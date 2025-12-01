# Incident Report
Generated: 2025-12-01T19:41:24.836431Z

## Summary

|   # | Type                  | IP            | Severity   | Rep Category   |   Rep Score | Notes                                                |
|-----|-----------------------|---------------|------------|----------------|-------------|------------------------------------------------------|
|   1 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /api/data (500)          |
|   2 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (500)             |
|   3 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (404)      |
|   4 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (404)             |
|   5 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (200)             |
|   6 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on / (500)                  |
|   7 | windows_logon_failure | 10.0.0.5      | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
|   8 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (200)             |
|   9 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (403)             |
|  10 | windows_logon_failure | 192.168.1.20  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
|  11 | windows_logon_failure | 198.51.100.23 | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
|  12 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /api/data (500)          |
|  13 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (403)      |
|  14 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on / (500)                  |
|  15 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (403)             |
|  16 | windows_logon_failure | 10.0.0.5      | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
|  17 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /api/data (500)          |
|  18 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /api/data (500)          |
|  19 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (200)      |
|  20 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (403)             |
|  21 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (301)      |
|  22 | windows_logon_failure | 192.168.1.20  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
|  23 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (200)      |
|  24 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /api/data (500)          |
|  25 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (301)      |
|  26 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (403)             |
|  27 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (200)             |
|  28 | windows_logon_failure | 10.0.0.12     | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
|  29 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (403)      |
|  30 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (301)             |
|  31 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (301)      |
|  32 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (404)             |
|  33 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (500)             |
|  34 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (404)             |
|  35 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (301)             |
|  36 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (500)             |
|  37 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (200)             |
|  38 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (403)             |
|  39 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /api/data (500)          |
|  40 | windows_logon_failure | 203.0.113.50  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
|  41 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (500)             |
|  42 | windows_logon_failure | 192.168.1.20  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
|  43 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (200)             |
|  44 | brute_force           | 203.0.113.50  | High       | unknown        |           0 | SSH brute force detected: 10 failed attempts         |
|  45 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (301)      |
|  46 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (403)      |
|  47 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (200)             |
|  48 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (404)             |
|  49 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (200)      |
|  50 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on / (403)                  |
|  51 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (403)             |
|  52 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (404)             |
|  53 | windows_logon_failure | 192.168.1.20  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
|  54 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on / (500)                  |
|  55 | windows_logon_failure | 10.0.0.12     | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
|  56 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /api/data (500)          |
|  57 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (200)      |
|  58 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on / (403)                  |
|  59 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (500)      |
|  60 | windows_logon_failure | 203.0.113.50  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
|  61 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (403)             |
|  62 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (200)      |
|  63 | brute_force           | 192.168.1.20  | High       | unknown        |           0 | SSH brute force detected: 10 failed attempts         |
|  64 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (404)             |
|  65 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (301)             |
|  66 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (403)             |
|  67 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (500)             |
|  68 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (200)             |
|  69 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (404)      |
|  70 | brute_force           | 198.51.100.23 | High       | unknown        |           0 | SSH brute force detected: 10 failed attempts         |
|  71 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (301)             |
|  72 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (500)             |
|  73 | windows_logon_failure | 203.0.113.50  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
|  74 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (403)             |
|  75 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (403)      |
|  76 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (403)             |
|  77 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on / (500)                  |
|  78 | brute_force           | 10.0.0.12     | High       | unknown        |           0 | SSH brute force detected: 10 failed attempts         |
|  79 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (200)             |
|  80 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on / (403)                  |
|  81 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (404)             |
|  82 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (200)      |
|  83 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /api/data (403)          |
|  84 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on / (500)                  |
|  85 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (200)      |
|  86 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (200)             |
|  87 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (404)             |
|  88 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (404)      |
|  89 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (404)             |
|  90 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (404)      |
|  91 | windows_logon_failure | 10.0.0.5      | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
|  92 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (403)             |
|  93 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (301)             |
|  94 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on / (403)                  |
|  95 | windows_logon_failure | 203.0.113.50  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
|  96 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (404)      |
|  97 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (500)      |
|  98 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (403)             |
|  99 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (500)      |
| 100 | windows_logon_failure | 192.168.1.20  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 101 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (200)             |
| 102 | windows_logon_failure | 192.168.1.20  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 103 | windows_logon_failure | 203.0.113.50  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 104 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (500)             |
| 105 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (403)      |
| 106 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (301)             |
| 107 | brute_force           | 203.0.113.99  | High       | unknown        |           0 | SSH brute force detected: 10 failed attempts         |
| 108 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (200)             |
| 109 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /api/data (403)          |
| 110 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (301)      |
| 111 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (500)             |
| 112 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (403)             |
| 113 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /api/data (500)          |
| 114 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (404)             |
| 115 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (200)             |
| 116 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /api/data (403)          |
| 117 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (500)             |
| 118 | windows_logon_failure | 198.51.100.23 | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 119 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (500)             |
| 120 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (301)             |
| 121 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (200)             |
| 122 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (200)             |
| 123 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (404)             |
| 124 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (404)             |
| 125 | windows_logon_failure | 192.168.1.20  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 126 | windows_logon_failure | 203.0.113.50  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 127 | windows_logon_failure | 192.168.1.20  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 128 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (301)      |
| 129 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (200)             |
| 130 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (404)      |
| 131 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (404)             |
| 132 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (404)      |
| 133 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /api/data (403)          |
| 134 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (404)             |
| 135 | windows_logon_failure | 203.0.113.50  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 136 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (403)             |
| 137 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (404)             |
| 138 | brute_force           | 203.0.113.50  | High       | unknown        |           0 | SSH brute force detected: 10 failed attempts         |
| 139 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /api/data (500)          |
| 140 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (404)      |
| 141 | windows_logon_failure | 10.0.0.5      | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 142 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (500)      |
| 143 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on / (403)                  |
| 144 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (404)             |
| 145 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (301)             |
| 146 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (404)             |
| 147 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (301)      |
| 148 | windows_logon_failure | 198.51.100.23 | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 149 | windows_logon_failure | 10.0.0.5      | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 150 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (301)      |
| 151 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (500)             |
| 152 | windows_logon_failure | 192.168.1.20  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 153 | windows_logon_failure | 203.0.113.50  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 154 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (404)      |
| 155 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (200)      |
| 156 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (200)      |
| 157 | brute_force           | 10.0.0.12     | High       | unknown        |           0 | SSH brute force detected: 10 failed attempts         |
| 158 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (403)             |
| 159 | windows_logon_failure | 192.168.1.20  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 160 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (404)             |
| 161 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (403)             |
| 162 | windows_logon_failure | 203.0.113.50  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 163 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (200)             |
| 164 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (500)      |
| 165 | windows_logon_failure | 10.0.0.5      | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 166 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on / (500)                  |
| 167 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (301)      |
| 168 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (200)      |
| 169 | brute_force           | 192.168.1.20  | High       | unknown        |           0 | SSH brute force detected: 10 failed attempts         |
| 170 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (500)             |
| 171 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (200)      |
| 172 | windows_logon_failure | 203.0.113.50  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 173 | windows_logon_failure | 192.168.1.20  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 174 | windows_logon_failure | 198.51.100.23 | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 175 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (403)             |
| 176 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (200)             |
| 177 | windows_logon_failure | 10.0.0.12     | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 178 | windows_logon_failure | 10.0.0.5      | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 179 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (200)             |
| 180 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /api/data (500)          |
| 181 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (404)      |
| 182 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (200)             |
| 183 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on / (500)                  |
| 184 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (200)             |
| 185 | windows_logon_failure | 203.0.113.50  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 186 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (200)             |
| 187 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (301)             |
| 188 | windows_logon_failure | 10.0.0.5      | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 189 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (301)             |
| 190 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (200)             |
| 191 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (500)             |
| 192 | windows_logon_failure | 203.0.113.50  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 193 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (301)             |
| 194 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (301)             |
| 195 | brute_force           | 198.51.100.23 | High       | unknown        |           0 | SSH brute force detected: 10 failed attempts         |
| 196 | windows_logon_failure | 192.168.1.20  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 197 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (500)      |
| 198 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (200)             |
| 199 | windows_logon_failure | 203.0.113.50  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 200 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (500)             |
| 201 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (301)      |
| 202 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (301)             |
| 203 | windows_logon_failure | 10.0.0.12     | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 204 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (403)             |
| 205 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (200)      |
| 206 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (200)             |
| 207 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (200)      |
| 208 | windows_logon_failure | 192.168.1.20  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 209 | windows_logon_failure | 10.0.0.12     | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 210 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (403)             |
| 211 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (301)             |
| 212 | windows_logon_failure | 198.51.100.23 | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 213 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (200)      |
| 214 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (200)             |
| 215 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (403)      |
| 216 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (200)      |
| 217 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (500)             |
| 218 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /api/data (403)          |
| 219 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (200)             |
| 220 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (200)      |
| 221 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (200)             |
| 222 | windows_logon_failure | 203.0.113.50  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 223 | windows_logon_failure | 10.0.0.12     | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 224 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on / (403)                  |
| 225 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (200)             |
| 226 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (500)      |
| 227 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on / (500)                  |
| 228 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (500)             |
| 229 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (404)             |
| 230 | windows_logon_failure | 198.51.100.23 | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 231 | brute_force           | 203.0.113.50  | High       | unknown        |           0 | SSH brute force detected: 10 failed attempts         |
| 232 | windows_logon_failure | 10.0.0.5      | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 233 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (404)             |
| 234 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on / (403)                  |
| 235 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on / (500)                  |
| 236 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (301)             |
| 237 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on / (500)                  |
| 238 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (403)             |
| 239 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (200)             |
| 240 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (301)             |
| 241 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (301)      |
| 242 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on / (403)                  |
| 243 | windows_logon_failure | 10.0.0.12     | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 244 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (404)      |
| 245 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (403)      |
| 246 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (200)             |
| 247 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (200)             |
| 248 | brute_force           | 10.0.0.5      | High       | unknown        |           0 | SSH brute force detected: 10 failed attempts         |
| 249 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (403)             |
| 250 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /api/data (403)          |
| 251 | windows_logon_failure | 10.0.0.5      | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 252 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (500)      |
| 253 | windows_logon_failure | 10.0.0.12     | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 254 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (301)      |
| 255 | windows_logon_failure | 10.0.0.12     | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 256 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on / (403)                  |
| 257 | brute_force           | 10.0.0.12     | High       | unknown        |           0 | SSH brute force detected: 10 failed attempts         |
| 258 | windows_logon_failure | 198.51.100.23 | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 259 | brute_force           | 192.168.1.20  | High       | unknown        |           0 | SSH brute force detected: 10 failed attempts         |
| 260 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on / (500)                  |
| 261 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /api/data (500)          |
| 262 | windows_logon_failure | 198.51.100.23 | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 263 | windows_logon_failure | 10.0.0.5      | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 264 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (500)             |
| 265 | windows_logon_failure | 10.0.0.5      | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 266 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (403)      |
| 267 | windows_logon_failure | 10.0.0.12     | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 268 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (200)      |
| 269 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (200)             |
| 270 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (301)      |
| 271 | windows_logon_failure | 192.168.1.20  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 272 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (200)      |
| 273 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /api/data (403)          |
| 274 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (403)      |
| 275 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (403)             |
| 276 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (500)             |
| 277 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on / (500)                  |
| 278 | windows_logon_failure | 10.0.0.5      | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 279 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (200)             |
| 280 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (404)             |
| 281 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (200)             |
| 282 | brute_force           | 203.0.113.50  | High       | unknown        |           0 | SSH brute force detected: 10 failed attempts         |
| 283 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (200)             |
| 284 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (200)             |
| 285 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on / (500)                  |
| 286 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (500)      |
| 287 | windows_logon_failure | 203.0.113.50  | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 288 | windows_logon_failure | 10.0.0.12     | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 289 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on / (403)                  |
| 290 | brute_force           | 198.51.100.23 | High       | unknown        |           0 | SSH brute force detected: 10 failed attempts         |
| 291 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on / (500)                  |
| 292 | windows_logon_failure | 198.51.100.23 | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 293 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /api/data (403)          |
| 294 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (200)      |
| 295 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (301)      |
| 296 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (500)             |
| 297 | windows_logon_failure | 10.0.0.5      | Low        | unknown        |           0 | Windows logon failure: Logon Failure                 |
| 298 | brute_force           | 203.0.113.99  | High       | unknown        |           0 | SSH brute force detected: 10 failed attempts         |
| 299 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (500)      |
| 300 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (403)             |
| 301 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /login (200)             |
| 302 | suspicious_http       | 10.0.0.12     | Medium     | unknown        |           0 | Suspicious HTTP activity on /api/data (403)          |
| 303 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /api/data (500)          |
| 304 | suspicious_http       | 203.0.113.50  | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (301)             |
| 305 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on /admin (500)             |
| 306 | suspicious_http       | 198.51.100.23 | Medium     | unknown        |           0 | Suspicious HTTP activity on / (403)                  |
| 307 | suspicious_http       | 192.168.1.20  | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (500)      |
| 308 | suspicious_http       | 10.0.0.5      | Medium     | unknown        |           0 | Suspicious HTTP activity on /wp-login.php (404)      |
| 309 | high_activity         | 10.0.0.12     | Medium     | unknown        |           0 | IP 10.0.0.12 generated 217 events (threshold 50)     |
| 310 | high_activity         | 192.168.1.20  | Medium     | unknown        |           0 | IP 192.168.1.20 generated 204 events (threshold 50)  |
| 311 | high_activity         | 198.51.100.23 | Medium     | unknown        |           0 | IP 198.51.100.23 generated 178 events (threshold 50) |
| 312 | high_activity         | 203.0.113.50  | Medium     | unknown        |           0 | IP 203.0.113.50 generated 208 events (threshold 50)  |
| 313 | high_activity         | 10.0.0.5      | Medium     | unknown        |           0 | IP 10.0.0.5 generated 193 events (threshold 50)      |


## Details

### Alert 1: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /api/data
- **code**: 500
- **description**: Suspicious HTTP activity on /api/data (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 2: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /login
- **code**: 500
- **description**: Suspicious HTTP activity on /login (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 3: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /wp-login.php
- **code**: 404
- **description**: Suspicious HTTP activity on /wp-login.php (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 4: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /admin
- **code**: 404
- **description**: Suspicious HTTP activity on /admin (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 5: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /login
- **code**: 200
- **description**: Suspicious HTTP activity on /login (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 6: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /
- **code**: 500
- **description**: Suspicious HTTP activity on / (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 7: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 10.0.0.5
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 8: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /admin
- **code**: 200
- **description**: Suspicious HTTP activity on /admin (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 9: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /admin
- **code**: 403
- **description**: Suspicious HTTP activity on /admin (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 10: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 192.168.1.20
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 11: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 198.51.100.23
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 12: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /api/data
- **code**: 500
- **description**: Suspicious HTTP activity on /api/data (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 13: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /wp-login.php
- **code**: 403
- **description**: Suspicious HTTP activity on /wp-login.php (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 14: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /
- **code**: 500
- **description**: Suspicious HTTP activity on / (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 15: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /admin
- **code**: 403
- **description**: Suspicious HTTP activity on /admin (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 16: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 10.0.0.5
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 17: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /api/data
- **code**: 500
- **description**: Suspicious HTTP activity on /api/data (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 18: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /api/data
- **code**: 500
- **description**: Suspicious HTTP activity on /api/data (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 19: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /wp-login.php
- **code**: 200
- **description**: Suspicious HTTP activity on /wp-login.php (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 20: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /login
- **code**: 403
- **description**: Suspicious HTTP activity on /login (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 21: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /wp-login.php
- **code**: 301
- **description**: Suspicious HTTP activity on /wp-login.php (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 22: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 192.168.1.20
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 23: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /wp-login.php
- **code**: 200
- **description**: Suspicious HTTP activity on /wp-login.php (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 24: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /api/data
- **code**: 500
- **description**: Suspicious HTTP activity on /api/data (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 25: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /wp-login.php
- **code**: 301
- **description**: Suspicious HTTP activity on /wp-login.php (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 26: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /login
- **code**: 403
- **description**: Suspicious HTTP activity on /login (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 27: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /login
- **code**: 200
- **description**: Suspicious HTTP activity on /login (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 28: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 10.0.0.12
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 29: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /wp-login.php
- **code**: 403
- **description**: Suspicious HTTP activity on /wp-login.php (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 30: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /admin
- **code**: 301
- **description**: Suspicious HTTP activity on /admin (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 31: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /wp-login.php
- **code**: 301
- **description**: Suspicious HTTP activity on /wp-login.php (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 32: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /admin
- **code**: 404
- **description**: Suspicious HTTP activity on /admin (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 33: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /admin
- **code**: 500
- **description**: Suspicious HTTP activity on /admin (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 34: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /admin
- **code**: 404
- **description**: Suspicious HTTP activity on /admin (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 35: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /login
- **code**: 301
- **description**: Suspicious HTTP activity on /login (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 36: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /admin
- **code**: 500
- **description**: Suspicious HTTP activity on /admin (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 37: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /admin
- **code**: 200
- **description**: Suspicious HTTP activity on /admin (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 38: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /login
- **code**: 403
- **description**: Suspicious HTTP activity on /login (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 39: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /api/data
- **code**: 500
- **description**: Suspicious HTTP activity on /api/data (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 40: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 203.0.113.50
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 41: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /admin
- **code**: 500
- **description**: Suspicious HTTP activity on /admin (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 42: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 192.168.1.20
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 43: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /admin
- **code**: 200
- **description**: Suspicious HTTP activity on /admin (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 44: brute_force
- **type**: brute_force
- **ip**: 203.0.113.50
- **count_in_window**: 10
- **first_detected**: 2025-12-01T19:25:23+00:00
- **last_detected**: 2025-12-01T17:51:26+00:00
- **description**: SSH brute force detected: 10 failed attempts
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 45: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /wp-login.php
- **code**: 301
- **description**: Suspicious HTTP activity on /wp-login.php (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 46: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /wp-login.php
- **code**: 403
- **description**: Suspicious HTTP activity on /wp-login.php (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 47: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /admin
- **code**: 200
- **description**: Suspicious HTTP activity on /admin (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 48: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /login
- **code**: 404
- **description**: Suspicious HTTP activity on /login (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 49: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /wp-login.php
- **code**: 200
- **description**: Suspicious HTTP activity on /wp-login.php (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 50: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /
- **code**: 403
- **description**: Suspicious HTTP activity on / (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 51: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /login
- **code**: 403
- **description**: Suspicious HTTP activity on /login (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 52: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /login
- **code**: 404
- **description**: Suspicious HTTP activity on /login (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 53: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 192.168.1.20
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 54: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /
- **code**: 500
- **description**: Suspicious HTTP activity on / (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 55: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 10.0.0.12
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 56: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /api/data
- **code**: 500
- **description**: Suspicious HTTP activity on /api/data (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 57: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /wp-login.php
- **code**: 200
- **description**: Suspicious HTTP activity on /wp-login.php (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 58: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /
- **code**: 403
- **description**: Suspicious HTTP activity on / (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 59: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /wp-login.php
- **code**: 500
- **description**: Suspicious HTTP activity on /wp-login.php (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 60: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 203.0.113.50
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 61: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /login
- **code**: 403
- **description**: Suspicious HTTP activity on /login (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 62: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /wp-login.php
- **code**: 200
- **description**: Suspicious HTTP activity on /wp-login.php (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 63: brute_force
- **type**: brute_force
- **ip**: 192.168.1.20
- **count_in_window**: 10
- **first_detected**: 2025-12-01T19:39:17+00:00
- **last_detected**: 2025-12-01T18:06:13+00:00
- **description**: SSH brute force detected: 10 failed attempts
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 64: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /login
- **code**: 404
- **description**: Suspicious HTTP activity on /login (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 65: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /admin
- **code**: 301
- **description**: Suspicious HTTP activity on /admin (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 66: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /login
- **code**: 403
- **description**: Suspicious HTTP activity on /login (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 67: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /admin
- **code**: 500
- **description**: Suspicious HTTP activity on /admin (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 68: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /admin
- **code**: 200
- **description**: Suspicious HTTP activity on /admin (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 69: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /wp-login.php
- **code**: 404
- **description**: Suspicious HTTP activity on /wp-login.php (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 70: brute_force
- **type**: brute_force
- **ip**: 198.51.100.23
- **count_in_window**: 10
- **first_detected**: 2025-12-01T19:25:16+00:00
- **last_detected**: 2025-12-01T19:17:25+00:00
- **description**: SSH brute force detected: 10 failed attempts
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 71: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /admin
- **code**: 301
- **description**: Suspicious HTTP activity on /admin (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 72: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /admin
- **code**: 500
- **description**: Suspicious HTTP activity on /admin (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 73: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 203.0.113.50
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 74: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /admin
- **code**: 403
- **description**: Suspicious HTTP activity on /admin (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 75: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /wp-login.php
- **code**: 403
- **description**: Suspicious HTTP activity on /wp-login.php (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 76: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /login
- **code**: 403
- **description**: Suspicious HTTP activity on /login (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 77: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /
- **code**: 500
- **description**: Suspicious HTTP activity on / (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 78: brute_force
- **type**: brute_force
- **ip**: 10.0.0.12
- **count_in_window**: 10
- **first_detected**: 2025-12-01T19:35:27+00:00
- **last_detected**: 2025-12-01T19:04:19+00:00
- **description**: SSH brute force detected: 10 failed attempts
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 79: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /admin
- **code**: 200
- **description**: Suspicious HTTP activity on /admin (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 80: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /
- **code**: 403
- **description**: Suspicious HTTP activity on / (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 81: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /login
- **code**: 404
- **description**: Suspicious HTTP activity on /login (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 82: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /wp-login.php
- **code**: 200
- **description**: Suspicious HTTP activity on /wp-login.php (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 83: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /api/data
- **code**: 403
- **description**: Suspicious HTTP activity on /api/data (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 84: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /
- **code**: 500
- **description**: Suspicious HTTP activity on / (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 85: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /wp-login.php
- **code**: 200
- **description**: Suspicious HTTP activity on /wp-login.php (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 86: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /login
- **code**: 200
- **description**: Suspicious HTTP activity on /login (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 87: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /admin
- **code**: 404
- **description**: Suspicious HTTP activity on /admin (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 88: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /wp-login.php
- **code**: 404
- **description**: Suspicious HTTP activity on /wp-login.php (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 89: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /login
- **code**: 404
- **description**: Suspicious HTTP activity on /login (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 90: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /wp-login.php
- **code**: 404
- **description**: Suspicious HTTP activity on /wp-login.php (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 91: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 10.0.0.5
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 92: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /login
- **code**: 403
- **description**: Suspicious HTTP activity on /login (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 93: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /admin
- **code**: 301
- **description**: Suspicious HTTP activity on /admin (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 94: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /
- **code**: 403
- **description**: Suspicious HTTP activity on / (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 95: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 203.0.113.50
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 96: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /wp-login.php
- **code**: 404
- **description**: Suspicious HTTP activity on /wp-login.php (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 97: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /wp-login.php
- **code**: 500
- **description**: Suspicious HTTP activity on /wp-login.php (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 98: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /admin
- **code**: 403
- **description**: Suspicious HTTP activity on /admin (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 99: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /wp-login.php
- **code**: 500
- **description**: Suspicious HTTP activity on /wp-login.php (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 100: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 192.168.1.20
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 101: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /login
- **code**: 200
- **description**: Suspicious HTTP activity on /login (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 102: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 192.168.1.20
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 103: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 203.0.113.50
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 104: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /admin
- **code**: 500
- **description**: Suspicious HTTP activity on /admin (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 105: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /wp-login.php
- **code**: 403
- **description**: Suspicious HTTP activity on /wp-login.php (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 106: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /login
- **code**: 301
- **description**: Suspicious HTTP activity on /login (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 107: brute_force
- **type**: brute_force
- **ip**: 203.0.113.99
- **count_in_window**: 10
- **first_detected**: 2025-12-01T19:10:46+00:00
- **last_detected**: 2025-12-01T19:11:21+00:00
- **description**: SSH brute force detected: 10 failed attempts
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 108: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /admin
- **code**: 200
- **description**: Suspicious HTTP activity on /admin (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 109: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /api/data
- **code**: 403
- **description**: Suspicious HTTP activity on /api/data (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 110: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /wp-login.php
- **code**: 301
- **description**: Suspicious HTTP activity on /wp-login.php (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 111: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /login
- **code**: 500
- **description**: Suspicious HTTP activity on /login (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 112: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /admin
- **code**: 403
- **description**: Suspicious HTTP activity on /admin (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 113: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /api/data
- **code**: 500
- **description**: Suspicious HTTP activity on /api/data (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 114: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /login
- **code**: 404
- **description**: Suspicious HTTP activity on /login (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 115: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /admin
- **code**: 200
- **description**: Suspicious HTTP activity on /admin (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 116: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /api/data
- **code**: 403
- **description**: Suspicious HTTP activity on /api/data (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 117: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /login
- **code**: 500
- **description**: Suspicious HTTP activity on /login (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 118: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 198.51.100.23
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 119: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /admin
- **code**: 500
- **description**: Suspicious HTTP activity on /admin (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 120: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /login
- **code**: 301
- **description**: Suspicious HTTP activity on /login (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 121: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /login
- **code**: 200
- **description**: Suspicious HTTP activity on /login (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 122: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /login
- **code**: 200
- **description**: Suspicious HTTP activity on /login (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 123: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /admin
- **code**: 404
- **description**: Suspicious HTTP activity on /admin (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 124: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /login
- **code**: 404
- **description**: Suspicious HTTP activity on /login (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 125: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 192.168.1.20
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 126: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 203.0.113.50
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 127: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 192.168.1.20
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 128: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /wp-login.php
- **code**: 301
- **description**: Suspicious HTTP activity on /wp-login.php (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 129: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /admin
- **code**: 200
- **description**: Suspicious HTTP activity on /admin (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 130: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /wp-login.php
- **code**: 404
- **description**: Suspicious HTTP activity on /wp-login.php (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 131: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /login
- **code**: 404
- **description**: Suspicious HTTP activity on /login (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 132: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /wp-login.php
- **code**: 404
- **description**: Suspicious HTTP activity on /wp-login.php (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 133: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /api/data
- **code**: 403
- **description**: Suspicious HTTP activity on /api/data (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 134: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /admin
- **code**: 404
- **description**: Suspicious HTTP activity on /admin (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 135: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 203.0.113.50
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 136: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /login
- **code**: 403
- **description**: Suspicious HTTP activity on /login (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 137: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /login
- **code**: 404
- **description**: Suspicious HTTP activity on /login (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 138: brute_force
- **type**: brute_force
- **ip**: 203.0.113.50
- **count_in_window**: 10
- **first_detected**: 2025-12-01T19:37:08+00:00
- **last_detected**: 2025-12-01T19:17:00+00:00
- **description**: SSH brute force detected: 10 failed attempts
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 139: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /api/data
- **code**: 500
- **description**: Suspicious HTTP activity on /api/data (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 140: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /wp-login.php
- **code**: 404
- **description**: Suspicious HTTP activity on /wp-login.php (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 141: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 10.0.0.5
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 142: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /wp-login.php
- **code**: 500
- **description**: Suspicious HTTP activity on /wp-login.php (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 143: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /
- **code**: 403
- **description**: Suspicious HTTP activity on / (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 144: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /login
- **code**: 404
- **description**: Suspicious HTTP activity on /login (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 145: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /admin
- **code**: 301
- **description**: Suspicious HTTP activity on /admin (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 146: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /login
- **code**: 404
- **description**: Suspicious HTTP activity on /login (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 147: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /wp-login.php
- **code**: 301
- **description**: Suspicious HTTP activity on /wp-login.php (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 148: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 198.51.100.23
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 149: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 10.0.0.5
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 150: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /wp-login.php
- **code**: 301
- **description**: Suspicious HTTP activity on /wp-login.php (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 151: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /admin
- **code**: 500
- **description**: Suspicious HTTP activity on /admin (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 152: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 192.168.1.20
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 153: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 203.0.113.50
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 154: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /wp-login.php
- **code**: 404
- **description**: Suspicious HTTP activity on /wp-login.php (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 155: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /wp-login.php
- **code**: 200
- **description**: Suspicious HTTP activity on /wp-login.php (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 156: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /wp-login.php
- **code**: 200
- **description**: Suspicious HTTP activity on /wp-login.php (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 157: brute_force
- **type**: brute_force
- **ip**: 10.0.0.12
- **count_in_window**: 10
- **first_detected**: 2025-12-01T19:34:20+00:00
- **last_detected**: 2025-12-01T18:50:47+00:00
- **description**: SSH brute force detected: 10 failed attempts
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 158: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /login
- **code**: 403
- **description**: Suspicious HTTP activity on /login (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 159: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 192.168.1.20
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 160: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /login
- **code**: 404
- **description**: Suspicious HTTP activity on /login (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 161: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /login
- **code**: 403
- **description**: Suspicious HTTP activity on /login (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 162: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 203.0.113.50
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 163: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /admin
- **code**: 200
- **description**: Suspicious HTTP activity on /admin (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 164: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /wp-login.php
- **code**: 500
- **description**: Suspicious HTTP activity on /wp-login.php (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 165: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 10.0.0.5
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 166: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /
- **code**: 500
- **description**: Suspicious HTTP activity on / (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 167: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /wp-login.php
- **code**: 301
- **description**: Suspicious HTTP activity on /wp-login.php (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 168: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /wp-login.php
- **code**: 200
- **description**: Suspicious HTTP activity on /wp-login.php (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 169: brute_force
- **type**: brute_force
- **ip**: 192.168.1.20
- **count_in_window**: 10
- **first_detected**: 2025-12-01T19:31:36+00:00
- **last_detected**: 2025-12-01T18:23:15+00:00
- **description**: SSH brute force detected: 10 failed attempts
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 170: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /login
- **code**: 500
- **description**: Suspicious HTTP activity on /login (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 171: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /wp-login.php
- **code**: 200
- **description**: Suspicious HTTP activity on /wp-login.php (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 172: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 203.0.113.50
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 173: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 192.168.1.20
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 174: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 198.51.100.23
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 175: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /admin
- **code**: 403
- **description**: Suspicious HTTP activity on /admin (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 176: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /login
- **code**: 200
- **description**: Suspicious HTTP activity on /login (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 177: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 10.0.0.12
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 178: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 10.0.0.5
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 179: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /admin
- **code**: 200
- **description**: Suspicious HTTP activity on /admin (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 180: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /api/data
- **code**: 500
- **description**: Suspicious HTTP activity on /api/data (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 181: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /wp-login.php
- **code**: 404
- **description**: Suspicious HTTP activity on /wp-login.php (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 182: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /admin
- **code**: 200
- **description**: Suspicious HTTP activity on /admin (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 183: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /
- **code**: 500
- **description**: Suspicious HTTP activity on / (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 184: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /login
- **code**: 200
- **description**: Suspicious HTTP activity on /login (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 185: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 203.0.113.50
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 186: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /login
- **code**: 200
- **description**: Suspicious HTTP activity on /login (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 187: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /admin
- **code**: 301
- **description**: Suspicious HTTP activity on /admin (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 188: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 10.0.0.5
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 189: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /admin
- **code**: 301
- **description**: Suspicious HTTP activity on /admin (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 190: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /admin
- **code**: 200
- **description**: Suspicious HTTP activity on /admin (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 191: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /login
- **code**: 500
- **description**: Suspicious HTTP activity on /login (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 192: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 203.0.113.50
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 193: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /admin
- **code**: 301
- **description**: Suspicious HTTP activity on /admin (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 194: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /login
- **code**: 301
- **description**: Suspicious HTTP activity on /login (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 195: brute_force
- **type**: brute_force
- **ip**: 198.51.100.23
- **count_in_window**: 10
- **first_detected**: 2025-12-01T19:26:04+00:00
- **last_detected**: 2025-12-01T18:44:00+00:00
- **description**: SSH brute force detected: 10 failed attempts
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 196: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 192.168.1.20
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 197: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /wp-login.php
- **code**: 500
- **description**: Suspicious HTTP activity on /wp-login.php (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 198: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /login
- **code**: 200
- **description**: Suspicious HTTP activity on /login (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 199: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 203.0.113.50
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 200: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /login
- **code**: 500
- **description**: Suspicious HTTP activity on /login (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 201: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /wp-login.php
- **code**: 301
- **description**: Suspicious HTTP activity on /wp-login.php (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 202: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /login
- **code**: 301
- **description**: Suspicious HTTP activity on /login (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 203: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 10.0.0.12
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 204: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /login
- **code**: 403
- **description**: Suspicious HTTP activity on /login (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 205: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /wp-login.php
- **code**: 200
- **description**: Suspicious HTTP activity on /wp-login.php (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 206: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /admin
- **code**: 200
- **description**: Suspicious HTTP activity on /admin (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 207: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /wp-login.php
- **code**: 200
- **description**: Suspicious HTTP activity on /wp-login.php (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 208: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 192.168.1.20
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 209: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 10.0.0.12
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 210: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /login
- **code**: 403
- **description**: Suspicious HTTP activity on /login (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 211: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /login
- **code**: 301
- **description**: Suspicious HTTP activity on /login (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 212: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 198.51.100.23
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 213: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /wp-login.php
- **code**: 200
- **description**: Suspicious HTTP activity on /wp-login.php (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 214: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /login
- **code**: 200
- **description**: Suspicious HTTP activity on /login (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 215: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /wp-login.php
- **code**: 403
- **description**: Suspicious HTTP activity on /wp-login.php (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 216: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /wp-login.php
- **code**: 200
- **description**: Suspicious HTTP activity on /wp-login.php (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 217: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /login
- **code**: 500
- **description**: Suspicious HTTP activity on /login (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 218: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /api/data
- **code**: 403
- **description**: Suspicious HTTP activity on /api/data (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 219: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /admin
- **code**: 200
- **description**: Suspicious HTTP activity on /admin (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 220: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /wp-login.php
- **code**: 200
- **description**: Suspicious HTTP activity on /wp-login.php (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 221: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /admin
- **code**: 200
- **description**: Suspicious HTTP activity on /admin (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 222: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 203.0.113.50
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 223: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 10.0.0.12
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 224: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /
- **code**: 403
- **description**: Suspicious HTTP activity on / (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 225: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /login
- **code**: 200
- **description**: Suspicious HTTP activity on /login (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 226: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /wp-login.php
- **code**: 500
- **description**: Suspicious HTTP activity on /wp-login.php (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 227: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /
- **code**: 500
- **description**: Suspicious HTTP activity on / (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 228: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /login
- **code**: 500
- **description**: Suspicious HTTP activity on /login (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 229: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /admin
- **code**: 404
- **description**: Suspicious HTTP activity on /admin (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 230: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 198.51.100.23
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 231: brute_force
- **type**: brute_force
- **ip**: 203.0.113.50
- **count_in_window**: 10
- **first_detected**: 2025-12-01T19:32:02+00:00
- **last_detected**: 2025-12-01T18:39:08+00:00
- **description**: SSH brute force detected: 10 failed attempts
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 232: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 10.0.0.5
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 233: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /admin
- **code**: 404
- **description**: Suspicious HTTP activity on /admin (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 234: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /
- **code**: 403
- **description**: Suspicious HTTP activity on / (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 235: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /
- **code**: 500
- **description**: Suspicious HTTP activity on / (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 236: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /login
- **code**: 301
- **description**: Suspicious HTTP activity on /login (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 237: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /
- **code**: 500
- **description**: Suspicious HTTP activity on / (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 238: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /admin
- **code**: 403
- **description**: Suspicious HTTP activity on /admin (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 239: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /admin
- **code**: 200
- **description**: Suspicious HTTP activity on /admin (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 240: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /login
- **code**: 301
- **description**: Suspicious HTTP activity on /login (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 241: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /wp-login.php
- **code**: 301
- **description**: Suspicious HTTP activity on /wp-login.php (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 242: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /
- **code**: 403
- **description**: Suspicious HTTP activity on / (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 243: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 10.0.0.12
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 244: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /wp-login.php
- **code**: 404
- **description**: Suspicious HTTP activity on /wp-login.php (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 245: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /wp-login.php
- **code**: 403
- **description**: Suspicious HTTP activity on /wp-login.php (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 246: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /login
- **code**: 200
- **description**: Suspicious HTTP activity on /login (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 247: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /login
- **code**: 200
- **description**: Suspicious HTTP activity on /login (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 248: brute_force
- **type**: brute_force
- **ip**: 10.0.0.5
- **count_in_window**: 10
- **first_detected**: 2025-12-01T19:33:59+00:00
- **last_detected**: 2025-12-01T19:13:57+00:00
- **description**: SSH brute force detected: 10 failed attempts
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 249: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /admin
- **code**: 403
- **description**: Suspicious HTTP activity on /admin (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 250: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /api/data
- **code**: 403
- **description**: Suspicious HTTP activity on /api/data (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 251: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 10.0.0.5
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 252: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /wp-login.php
- **code**: 500
- **description**: Suspicious HTTP activity on /wp-login.php (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 253: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 10.0.0.12
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 254: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /wp-login.php
- **code**: 301
- **description**: Suspicious HTTP activity on /wp-login.php (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 255: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 10.0.0.12
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 256: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /
- **code**: 403
- **description**: Suspicious HTTP activity on / (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 257: brute_force
- **type**: brute_force
- **ip**: 10.0.0.12
- **count_in_window**: 10
- **first_detected**: 2025-12-01T19:37:46+00:00
- **last_detected**: 2025-12-01T19:03:54+00:00
- **description**: SSH brute force detected: 10 failed attempts
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 258: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 198.51.100.23
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 259: brute_force
- **type**: brute_force
- **ip**: 192.168.1.20
- **count_in_window**: 10
- **first_detected**: 2025-12-01T19:36:55+00:00
- **last_detected**: 2025-12-01T18:40:12+00:00
- **description**: SSH brute force detected: 10 failed attempts
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 260: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /
- **code**: 500
- **description**: Suspicious HTTP activity on / (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 261: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /api/data
- **code**: 500
- **description**: Suspicious HTTP activity on /api/data (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 262: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 198.51.100.23
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 263: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 10.0.0.5
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 264: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /admin
- **code**: 500
- **description**: Suspicious HTTP activity on /admin (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 265: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 10.0.0.5
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 266: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /wp-login.php
- **code**: 403
- **description**: Suspicious HTTP activity on /wp-login.php (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 267: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 10.0.0.12
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 268: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /wp-login.php
- **code**: 200
- **description**: Suspicious HTTP activity on /wp-login.php (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 269: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /login
- **code**: 200
- **description**: Suspicious HTTP activity on /login (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 270: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /wp-login.php
- **code**: 301
- **description**: Suspicious HTTP activity on /wp-login.php (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 271: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 192.168.1.20
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 272: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /wp-login.php
- **code**: 200
- **description**: Suspicious HTTP activity on /wp-login.php (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 273: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /api/data
- **code**: 403
- **description**: Suspicious HTTP activity on /api/data (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 274: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /wp-login.php
- **code**: 403
- **description**: Suspicious HTTP activity on /wp-login.php (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 275: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /login
- **code**: 403
- **description**: Suspicious HTTP activity on /login (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 276: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /admin
- **code**: 500
- **description**: Suspicious HTTP activity on /admin (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 277: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /
- **code**: 500
- **description**: Suspicious HTTP activity on / (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 278: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 10.0.0.5
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 279: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /login
- **code**: 200
- **description**: Suspicious HTTP activity on /login (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 280: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /login
- **code**: 404
- **description**: Suspicious HTTP activity on /login (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 281: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /login
- **code**: 200
- **description**: Suspicious HTTP activity on /login (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 282: brute_force
- **type**: brute_force
- **ip**: 203.0.113.50
- **count_in_window**: 10
- **first_detected**: 2025-12-01T19:34:05+00:00
- **last_detected**: 2025-12-01T19:34:54+00:00
- **description**: SSH brute force detected: 10 failed attempts
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 283: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /admin
- **code**: 200
- **description**: Suspicious HTTP activity on /admin (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 284: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /login
- **code**: 200
- **description**: Suspicious HTTP activity on /login (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 285: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /
- **code**: 500
- **description**: Suspicious HTTP activity on / (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 286: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /wp-login.php
- **code**: 500
- **description**: Suspicious HTTP activity on /wp-login.php (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 287: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 203.0.113.50
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 288: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 10.0.0.12
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 289: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /
- **code**: 403
- **description**: Suspicious HTTP activity on / (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 290: brute_force
- **type**: brute_force
- **ip**: 198.51.100.23
- **count_in_window**: 10
- **first_detected**: 2025-12-01T19:30:36+00:00
- **last_detected**: 2025-12-01T19:03:22+00:00
- **description**: SSH brute force detected: 10 failed attempts
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 291: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /
- **code**: 500
- **description**: Suspicious HTTP activity on / (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 292: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 198.51.100.23
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 293: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /api/data
- **code**: 403
- **description**: Suspicious HTTP activity on /api/data (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 294: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /wp-login.php
- **code**: 200
- **description**: Suspicious HTTP activity on /wp-login.php (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 295: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /wp-login.php
- **code**: 301
- **description**: Suspicious HTTP activity on /wp-login.php (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 296: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /login
- **code**: 500
- **description**: Suspicious HTTP activity on /login (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 297: windows_logon_failure
- **type**: windows_logon_failure
- **ip**: 10.0.0.5
- **msg**: Logon Failure
- **description**: Windows logon failure: Logon Failure
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 298: brute_force
- **type**: brute_force
- **ip**: 203.0.113.99
- **count_in_window**: 10
- **first_detected**: 2025-12-01T19:10:11+00:00
- **last_detected**: 2025-12-01T19:09:46+00:00
- **description**: SSH brute force detected: 10 failed attempts
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 299: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /wp-login.php
- **code**: 500
- **description**: Suspicious HTTP activity on /wp-login.php (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 300: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /admin
- **code**: 403
- **description**: Suspicious HTTP activity on /admin (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 301: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /login
- **code**: 200
- **description**: Suspicious HTTP activity on /login (200)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 302: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.12
- **path**: /api/data
- **code**: 403
- **description**: Suspicious HTTP activity on /api/data (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 303: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /api/data
- **code**: 500
- **description**: Suspicious HTTP activity on /api/data (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 304: suspicious_http
- **type**: suspicious_http
- **ip**: 203.0.113.50
- **path**: /admin
- **code**: 301
- **description**: Suspicious HTTP activity on /admin (301)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 305: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /admin
- **code**: 500
- **description**: Suspicious HTTP activity on /admin (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 306: suspicious_http
- **type**: suspicious_http
- **ip**: 198.51.100.23
- **path**: /
- **code**: 403
- **description**: Suspicious HTTP activity on / (403)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 307: suspicious_http
- **type**: suspicious_http
- **ip**: 192.168.1.20
- **path**: /wp-login.php
- **code**: 500
- **description**: Suspicious HTTP activity on /wp-login.php (500)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 308: suspicious_http
- **type**: suspicious_http
- **ip**: 10.0.0.5
- **path**: /wp-login.php
- **code**: 404
- **description**: Suspicious HTTP activity on /wp-login.php (404)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 309: high_activity
- **type**: high_activity
- **ip**: 10.0.0.12
- **count**: 217
- **description**: IP 10.0.0.12 generated 217 events (threshold 50)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 310: high_activity
- **type**: high_activity
- **ip**: 192.168.1.20
- **count**: 204
- **description**: IP 192.168.1.20 generated 204 events (threshold 50)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 311: high_activity
- **type**: high_activity
- **ip**: 198.51.100.23
- **count**: 178
- **description**: IP 198.51.100.23 generated 178 events (threshold 50)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 312: high_activity
- **type**: high_activity
- **ip**: 203.0.113.50
- **count**: 208
- **description**: IP 203.0.113.50 generated 208 events (threshold 50)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

### Alert 313: high_activity
- **type**: high_activity
- **ip**: 10.0.0.5
- **count**: 193
- **description**: IP 10.0.0.5 generated 193 events (threshold 50)
- **reputation.score**: 0
- **reputation.category**: unknown
- **reputation.details**: No local threat intel available

## Playbook

- Isolar IP suspeito
- Resetar credenciais afetadas
- Coletar evidências e consolidar logs
- Notificar equipe N2/SecOps
- Revisar políticas de segurança
