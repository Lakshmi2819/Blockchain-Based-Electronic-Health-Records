// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PatientConsent {
    struct Consent {
        address patient;
        address provider;
        bytes32 dataHash;
        uint256 timestamp;
        bool granted;
    }

    mapping(address => Consent[]) public consents;

    function grantAccess(address _provider, bytes32 _dataHash) public {
        consents[msg.sender].push(Consent(
            msg.sender, _provider, _dataHash, block.timestamp, true
        ));
    }

    function revokeAccess(address _provider, bytes32 _dataHash) public {
        Consent[] storage cList = consents[msg.sender];
        for (uint i = 0; i < cList.length; i++) {
            if (cList[i].provider == _provider && cList[i].dataHash == _dataHash) {
                cList[i].granted = false;
            }
        }
    }

    function getConsents(address _patient) public view returns (Consent[] memory) {
        return consents[_patient];
    }
}
