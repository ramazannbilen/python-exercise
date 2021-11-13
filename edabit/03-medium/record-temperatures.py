"""Record Temperatures
You are given two lists that each contain data that represents the min and max weather temperatures for each day of the week.

The records list contains the all-time record low/high temperatures for that day of the week.

[[record low, record high], ...]
The current week list contains the daily low/high temperatures for each day of the current week.

[[daily low, daily high], ...]
A daily high temperature is considered a new record high if it is higher than the record high for that day of the week. A daily low temperature is considered a new record low if it is lower than the record low for that day of the week.

Compare the daily low/high temperatures of the current week to the record lows/highs and return a list with the updated record temperatures.

There may be multiple record temperatures in a week.
If there are no broken records return the original records list.
Example
#             sun       mon      tues       wed      thur      fri       sat
record_temps([[34, 82], [24, 82], [20, 89],  [5, 88],  [9, 88], [26, 89], [27, 83]],
            [[44, 72], [19, 70], [40, 69], [39, 68], [33, 64], [36, 70], [38, 69]])

➞           [[34, 82], [19, 82], [20, 89], [5, 88], [9, 88], [26, 89], [27, 83]]
The previous record low for Monday was 24. The current week's low for Monday was 19. So 19 replaces 24 as Monday's new record low.

Notes
There won't be a record high and record low set on the same day.
Index 0 will always be the low and index 1 will always be the high [low, high].
For reference these temps are °F but you do not need to convert any temperatures."""

from edabit.Test import Test

def record_temps(records, currentWeek):
    cmax = []
    cmin = []
    for i in range(len(records)):
        if max(currentWeek[i]) >= max(records[i]):
            cmax.append(max(currentWeek[i]))
        else:
            cmax.append(max(records[i]))
        if min(currentWeek[i]) <= min(records[i]):
            cmin.append(min(currentWeek[i]))
        else:
            cmin.append(min(records[i]))
    res = []
    for i in range(len(cmin)):
        res.append([cmin[i], cmax[i]])
    return res


Test.assert_equals(record_temps([[34, 82], [24, 82], [20, 89], [5, 88], [9, 88], [26, 89], [27, 83]],
                                [[44, 72], [19, 70], [40, 69], [39, 68], [33, 64], [36, 70], [38, 69]]),
                   [[34, 82], [19, 82], [20, 89], [5, 88], [9, 88], [26, 89], [27, 83]]);
Test.assert_equals(record_temps(
    [
        [25, 80],
        [27, 88],
        [19, 88],
        [23, 85],
        [21, 89],
        [23, 78],
        [17, 79],
    ],
    [
        [40, 70],
        [41, 68],
        [45, 68],
        [39, 65],
        [44, 72],
        [43, 69],
        [37, 68],
    ]
), [
    [25, 80],
    [27, 88],
    [19, 88],
    [23, 85],
    [21, 89],
    [23, 78],
    [17, 79],
])
Test.assert_equals(record_temps(
    [
        [19, 78],
        [21, 79],
        [22, 90],
        [21, 79],
        [30, 86],
        [25, 82],
        [19, 80],
    ],
    [
        [29, 68],
        [24, 69],
        [28, 63],
        [20, 50],
        [25, 65],
        [28, 56],
        [30, 61],
    ]
), [
    [19, 78],
    [21, 79],
    [22, 90],
    [20, 79],
    [25, 86],
    [25, 82],
    [19, 80],
])
Test.assert_equals(record_temps(
    [
        [29, 90],
        [19, 78],
        [26, 91],
        [20, 86],
        [29, 79],
        [16, 84],
        [24, 83],
    ],
    [
        [33, 68],
        [38, 58],
        [36, 59],
        [40, 56],
        [37, 69],
        [39, 70],
        [41, 69],
    ]
), [
    [29, 90],
    [19, 78],
    [26, 91],
    [20, 86],
    [29, 79],
    [16, 84],
    [24, 83],
])
Test.assert_equals(record_temps(
    [
        [17, 84],
        [17, 90],
        [28, 85],
        [15, 89],
        [21, 80],
        [6, 86],
        [28, 87],
    ],
    [
        [27, 64],
        [31, 60],
        [33, 59],
        [35, 63],
        [32, 60],
        [35, 66],
        [25, 53],
    ]
), [
    [17, 84],
    [17, 90],
    [28, 85],
    [15, 89],
    [21, 80],
    [6, 86],
    [25, 87],
])
Test.assert_equals(record_temps(
    [
        [30, 88],
        [19, 89],
        [17, 79],
        [26, 93],
        [24, 84],
        [30, 90],
        [17, 90],
    ],
    [
        [33, 60],
        [29, 69],
        [34, 58],
        [36, 55],
        [30, 53],
        [28, 60],
        [29, 62],
    ]
), [
    [30, 88],
    [19, 89],
    [17, 79],
    [26, 93],
    [24, 84],
    [28, 90],
    [17, 90],
])
Test.assert_equals(record_temps(
    [
        [22, 91],
        [13, 79],
        [11, 80],
        [30, 91],
        [18, 77],
        [19, 85],
        [7, 87],
    ],
    [
        [32, 61],
        [23, 69],
        [31, 70],
        [31, 66],
        [28, 59],
        [27, 55],
        [23, 51],
    ]
), [
    [22, 91],
    [13, 79],
    [11, 80],
    [30, 91],
    [18, 77],
    [19, 85],
    [7, 87],
])
Test.assert_equals(record_temps(
    [
        [39, 103],
        [38, 99],
        [38, 104],
        [31, 99],
        [34, 103],
        [36, 101],
        [35, 99],
    ],
    [
        [53, 93],
        [58, 91],
        [49, 94],
        [51, 95],
        [54, 95],
        [56, 98],
        [60, 99],
    ]
), [
    [39, 103],
    [38, 99],
    [38, 104],
    [31, 99],
    [34, 103],
    [36, 101],
    [35, 99],
])
Test.assert_equals(record_temps(
    [
        [42, 106],
        [37, 97],
        [31, 101],
        [30, 100],
        [38, 101],
        [29, 98],
        [27, 99],
    ],
    [
        [52, 93],
        [61, 91],
        [60, 95],
        [60, 97],
        [68, 93],
        [70, 100],
        [57, 96],
    ]
), [
    [42, 106],
    [37, 97],
    [31, 101],
    [30, 100],
    [38, 101],
    [29, 100],
    [27, 99],
])
Test.assert_equals(record_temps(
    [
        [40, 98],
        [30, 100],
        [35, 100],
        [29, 105],
        [33, 100],
        [27, 96],
        [29, 97],
    ],
    [
        [60, 97],
        [57, 99],
        [65, 98],
        [59, 97],
        [63, 101],
        [57, 93],
        [69, 100],
    ]
), [
    [40, 98],
    [30, 100],
    [35, 100],
    [29, 105],
    [33, 101],
    [27, 96],
    [29, 100],
])
Test.assert_equals(record_temps(
    [
        [45, 99],
        [32, 99],
        [32, 102],
        [28, 103],
        [31, 99],
        [34, 104],
        [32, 100],
    ],
    [
        [65, 94],
        [62, 94],
        [72, 100],
        [68, 100],
        [71, 96],
        [69, 100],
        [72, 99],
    ]
), [
    [45, 99],
    [32, 99],
    [32, 102],
    [28, 103],
    [31, 99],
    [34, 104],
    [32, 100],
])
Test.assert_equals(record_temps(
    [
        [39, 101],
        [35, 98],
        [30, 97],
        [33, 103],
        [29, 98],
        [36, 97],
        [30, 103],
    ],
    [
        [69, 100],
        [65, 97],
        [70, 95],
        [73, 100],
        [75, 99],
        [73, 100],
        [70, 100],
    ]
), [
    [39, 101],
    [35, 98],
    [30, 97],
    [33, 103],
    [29, 99],
    [36, 100],
    [30, 103],
])
Test.assert_equals(record_temps(
    [
        [50, 105],
        [40, 100],
        [24, 99],
        [29, 99],
        [38, 100],
        [31, 100],
        [33, 100],
    ],
    [
        [70, 102],
        [70, 101],
        [69, 97],
        [68, 98],
        [71, 100],
        [72, 103],
        [73, 102],
    ]
), [
    [50, 105],
    [40, 101],
    [24, 99],
    [29, 99],
    [38, 100],
    [31, 103],
    [33, 102],
])
Test.assert_equals(record_temps(
    [
        [37, 100],
        [31, 104],
        [38, 102],
        [30, 97],
        [40, 107],
        [29, 99],
        [28, 101],
    ],
    [
        [71, 98],
        [71, 100],
        [72, 101],
        [70, 99],
        [68, 99],
        [69, 97],
        [69, 99],
    ]
), [
    [37, 100],
    [31, 104],
    [38, 102],
    [30, 99],
    [40, 107],
    [29, 99],
    [28, 101],
])
Test.assert_equals(record_temps(
    [
        [32, 99],
        [40, 97],
        [25, 101],
        [34, 97],
        [19, 103],
        [35, 98],
        [36, 102],
    ],
    [
        [72, 96],
        [70, 99],
        [65, 100],
        [71, 97],
        [73, 99],
        [65, 100],
        [66, 100],
    ]
), [
    [32, 99],
    [40, 99],
    [25, 101],
    [34, 97],
    [19, 103],
    [35, 100],
    [36, 102],
])
Test.assert_equals(record_temps(
    [
        [42, 98],
        [35, 105],
        [29, 98],
        [33, 104],
        [29, 104],
        [30, 102],
        [32, 98],
    ],
    [
        [62, 98],
        [69, 101],
        [68, 96],
        [73, 100],
        [69, 100],
        [70, 99],
        [72, 97],
    ]
), [
    [42, 98],
    [35, 105],
    [29, 98],
    [33, 104],
    [29, 104],
    [30, 102],
    [32, 98],
])

