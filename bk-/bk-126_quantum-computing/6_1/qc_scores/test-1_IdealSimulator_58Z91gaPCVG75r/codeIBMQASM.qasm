//OPENQASM 2.0
OPENQASM 2.0;

include "qelib1.inc";

qreg q[2];
creg c[2];

measure q[0] -> c[0];
