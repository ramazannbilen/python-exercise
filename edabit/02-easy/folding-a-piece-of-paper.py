"""
Folding a Piece of Paper
Create a function that
returns the thickness (in meters) of a piece of paper
after folding it n number of times.
The paper starts off with a thickness of 0.5mm.

Examples
num_layers(1) ➞ "0.001m"
# Paper folded once is 1mm (equal to 0.001m)

num_layers(4) ➞ "0.008m"
# Paper folded 4 times is 8mm (equal to 0.008m)

num_layers(21) ➞ "1048.576m"
# Paper folded 21 times is 1048576mm (equal to 1048.576m)
Notes
There are 1000mm in a single meter.
Don't round answers.
"""

from edabit.Test import Test


def num_layers(n):
    layer = 0.0005
    meter = "m"
    for i in range(n):
        layer *= 2
    return str(layer)+meter


if __name__ == '__main__':
    Test.assert_equals(num_layers(0), "0.0005m")
    Test.assert_equals(num_layers(1), "0.001m")
    Test.assert_equals(num_layers(2), "0.002m")
    Test.assert_equals(num_layers(3), "0.004m")
    Test.assert_equals(num_layers(4), "0.008m")
    Test.assert_equals(num_layers(5), "0.016m")
    Test.assert_equals(num_layers(6), "0.032m")
    Test.assert_equals(num_layers(7), "0.064m")
    Test.assert_equals(num_layers(8), "0.128m")
    Test.assert_equals(num_layers(9), "0.256m")
    Test.assert_equals(num_layers(10), "0.512m")
    Test.assert_equals(num_layers(11), "1.024m")
    Test.assert_equals(num_layers(12), "2.048m")
    Test.assert_equals(num_layers(13), "4.096m")
    Test.assert_equals(num_layers(14), "8.192m")
    Test.assert_equals(num_layers(15), "16.384m")
    Test.assert_equals(num_layers(16), "32.768m")
    Test.assert_equals(num_layers(17), "65.536m")
    Test.assert_equals(num_layers(18), "131.072m")
    Test.assert_equals(num_layers(19), "262.144m")
    Test.assert_equals(num_layers(20), "524.288m")
    Test.assert_equals(num_layers(21), "1048.576m")
    Test.assert_equals(num_layers(22), "2097.152m")
    Test.assert_equals(num_layers(23), "4194.304m")
    Test.assert_equals(num_layers(24), "8388.608m")
    Test.assert_equals(num_layers(25), "16777.216m")
    Test.assert_equals(num_layers(26), "33554.432m")
    Test.assert_equals(num_layers(27), "67108.864m")
    Test.assert_equals(num_layers(28), "134217.728m")
    Test.assert_equals(num_layers(29), "268435.456m")
    Test.assert_equals(num_layers(30), "536870.912m")
    Test.assert_equals(num_layers(31), "1073741.824m")
    Test.assert_equals(num_layers(32), "2147483.648m")
    Test.assert_equals(num_layers(33), "4294967.296m")
    Test.assert_equals(num_layers(34), "8589934.592m")
    Test.assert_equals(num_layers(35), "17179869.184m")
    Test.assert_equals(num_layers(36), "34359738.368m")
    Test.assert_equals(num_layers(37), "68719476.736m")
    Test.assert_equals(num_layers(38), "137438953.472m")
    Test.assert_equals(num_layers(39), "274877906.944m")
    Test.assert_equals(num_layers(40), "549755813.888m")
    Test.assert_equals(num_layers(41), "1099511627.776m")
    Test.assert_equals(num_layers(42), "2199023255.552m")
    Test.assert_equals(num_layers(43), "4398046511.104m")
    Test.assert_equals(num_layers(44), "8796093022.208m")
    Test.assert_equals(num_layers(45), "17592186044.416m")
    Test.assert_equals(num_layers(46), "35184372088.832m")
    Test.assert_equals(num_layers(47), "70368744177.664m")
    Test.assert_equals(num_layers(48), "140737488355.328m")
    Test.assert_equals(num_layers(49), "281474976710.656m")
    Test.assert_equals(num_layers(50), "562949953421.312m")
    Test.assert_equals(num_layers(51), "1125899906842.624m")
    Test.assert_equals(num_layers(52), "2251799813685.248m")
    Test.assert_equals(num_layers(53), "4503599627370.496m")
    Test.assert_equals(num_layers(54), "9007199254740.992m")
    Test.assert_equals(num_layers(55), "18014398509481.984m")
    Test.assert_equals(num_layers(56), "36028797018963.97m")
    Test.assert_equals(num_layers(57), "72057594037927.94m")
    Test.assert_equals(num_layers(58), "144115188075855.88m")
    Test.assert_equals(num_layers(59), "288230376151711.75m")
    Test.assert_equals(num_layers(60), "576460752303423.5m")
    Test.assert_equals(num_layers(61), "1152921504606847.0m")
    Test.assert_equals(num_layers(62), "2305843009213694.0m")
    Test.assert_equals(num_layers(63), "4611686018427388.0m")
    Test.assert_equals(num_layers(64), "9223372036854776.0m")
    Test.assert_equals(num_layers(65), "1.844674407370955e+16m")
    Test.assert_equals(num_layers(66), "3.68934881474191e+16m")
    Test.assert_equals(num_layers(67), "7.37869762948382e+16m")
    Test.assert_equals(num_layers(68), "1.475739525896764e+17m")
    Test.assert_equals(num_layers(69), "2.951479051793528e+17m")
    Test.assert_equals(num_layers(70), "5.902958103587057e+17m")
    Test.assert_equals(num_layers(71), "1.1805916207174113e+18m")
    Test.assert_equals(num_layers(72), "2.3611832414348227e+18m")
    Test.assert_equals(num_layers(73), "4.722366482869645e+18m")
    Test.assert_equals(num_layers(74), "9.44473296573929e+18m")
    Test.assert_equals(num_layers(75), "1.888946593147858e+19m")
    Test.assert_equals(num_layers(76), "3.777893186295716e+19m")
    Test.assert_equals(num_layers(77), "7.555786372591432e+19m")
    Test.assert_equals(num_layers(78), "1.5111572745182865e+20m")
    Test.assert_equals(num_layers(79), "3.022314549036573e+20m")
    Test.assert_equals(num_layers(80), "6.044629098073146e+20m")
    Test.assert_equals(num_layers(81), "1.2089258196146292e+21m")
    Test.assert_equals(num_layers(82), "2.4178516392292584e+21m")
    Test.assert_equals(num_layers(83), "4.835703278458517e+21m")
    Test.assert_equals(num_layers(84), "9.671406556917034e+21m")
    Test.assert_equals(num_layers(85), "1.9342813113834067e+22m")
    Test.assert_equals(num_layers(86), "3.8685626227668134e+22m")
    Test.assert_equals(num_layers(87), "7.737125245533627e+22m")
    Test.assert_equals(num_layers(88), "1.5474250491067254e+23m")
    Test.assert_equals(num_layers(89), "3.094850098213451e+23m")
    Test.assert_equals(num_layers(90), "6.189700196426902e+23m")
    Test.assert_equals(num_layers(91), "1.2379400392853803e+24m")
    Test.assert_equals(num_layers(92), "2.4758800785707606e+24m")
    Test.assert_equals(num_layers(93), "4.951760157141521e+24m")
    Test.assert_equals(num_layers(94), "9.903520314283042e+24m")
    Test.assert_equals(num_layers(95), "1.9807040628566085e+25m")
    Test.assert_equals(num_layers(96), "3.961408125713217e+25m")
    Test.assert_equals(num_layers(97), "7.922816251426434e+25m")
    Test.assert_equals(num_layers(98), "1.5845632502852868e+26m")
    Test.assert_equals(num_layers(99), "3.1691265005705736e+26m")
    Test.assert_equals(num_layers(100), "6.338253001141147e+26m")
