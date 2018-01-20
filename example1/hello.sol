pragma solidity ^0.4.0;

contract Hello {
	string public hello='Hello world!';

	function Hello() public {
		hello;
	}

	function setString(string _myString) public {
		hello = _myString;
	}

	function getString() public returns (string) {
		return hello;
	}
}