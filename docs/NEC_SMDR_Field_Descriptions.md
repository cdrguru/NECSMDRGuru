## KA RECORD

**Description:** The KA SMDR Record is a normal format record that captures comprehensive details of outgoing calls, including the route and trunk used, caller identification, call duration, account and authorization codes, the called party's number, metering pulse data, and ISDN charge information.

| CHARACTER | SMDR FIELD NAME AND DESCRIPTION | SMDR FIELD NAME COMMENT |
|---------------------------|----------------------------------|-------------------------|
| 000 | STX | Start of Text |
| 001 | SA | System Address; fixed data |
| 002 | UA | Unit Address |
| 003 | Entry Index “K” | “K” = SMDR record |
| 004 | Type of Record “A” | “A” = Outgoing Call / Normal Format |
| 005 | Route Number – Hundredths | Outgoing Route and Trunk information |
| 006 | Route Number – Tenths | Outgoing Route and Trunk information |
| 007 | Route Number – Ones | Outgoing Route and Trunk information |
| 008 | Trunk Number – Hundredths | Outgoing Route and Trunk information |
| 009 | Trunk Number – Tenths | Outgoing Route and Trunk information |
| 010 | Trunk Number – Ones | Outgoing Route and Trunk information |
| 011 | Calling Party Identification | 0 = PBX/CTX (DID) station
1 = Attendant Console
2 = Incoming Trunk
3 = Monitored Number (See Appendix D) |
| 012 | Tenant – 1st digit | Only in 1000 & 2000 (RDS) Feature Packages. 3000 (RDS) and above, fields are blank. |
| 013 | Tenant – 2nd digit | Represents the second digit of the tenant code in multi-tenant environments. |
| 014 | Calling Number – 1 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 011 is;
0 – Station number is shown1
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 015 | Calling Number – 2 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 011 is;
0 – Station number is shown1
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 016 | Calling Number – 3 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 011 is;
0 – Station number is shown1
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 017 | Calling Number – 4 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 011 is;
0 – Station number is shown1
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 018 | Calling Number – 5 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 011 is;
0 – Station number is shown1
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 019 | Calling Number – 6 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 011 is;
0 – Station number is shown1
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 020 | Month – Tenths | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 021 | Month – Ones | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 022 | Day – Tenths | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 023 | Day – Ones | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 024 | Hour – Tenths | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 025 | Hour – Ones | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 026 | Minute – Tenths | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 027 | Minute – Ones | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 028 | Second – Tenths | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 029 | Second – Ones | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 030 | Month –Tenths | Time when SMDR record is complete |
| 031 | Month – Ones | Time when SMDR record is complete |
| 032 | Day – Tenths | Time when SMDR record is complete |
| 033 | Day – Ones | Time when SMDR record is complete |
| 034 | Hour – Tenths | Time when SMDR record is complete |
| 035 | Hour – Ones | Time when SMDR record is complete |
| 036 | Minute – Tenths | Time when SMDR record is complete |
| 037 | Minute – Ones | Time when SMDR record is complete |
| 038 | Second – Tenths | Time when SMDR record is complete |
| 039 | Second – Ones | Time when SMDR record is complete |
| 040~049 | Account Code (max 10 digits) | Blank if Account Code not present |
| 050 | Tenant – 1st digit | Calling Party Tenant Information
This is for 3000 (RDS) Series Feature Package and higher. |
| 051 | Tenant – 2nd digit | Calling Party Tenant Information
This is for 3000 (RDS) Series Feature Package and higher. |
| 052 | Tenant – 3rd digit | Calling Party Tenant Information
This is for 3000 (RDS) Series Feature Package and higher. |
| 053 | Condition Code One | 0 = Call has not transferred
1 = Call has been transferred Example:
Station-A calls Station-B, talks for 10 minutes then transfers outside to Station-C. The SMDR record will show Condition 1.
(Note: ASYD System 1 Index 33 will effect who is billed on a transfer) |
| 054 | Condition Code Two | 0 = Incoming, Outgoing, or Tandem call with neither Outgoing Trunk Queuing nor Account Codes used.
1 = Outgoing Trunk Queuing used, but not Account Codes.
2 = Account Codes used, but not Outgoing Trunk Queuing.
3 = Both Outgoing Trunk Queuing and Account Codes used. |
| 055 | Condition Code Three | 0 = Regular Outgoing or Tandem call.
1 = Attendant Operator assisted call.
2 = The call Route Advanced (AOPR).
3 = Attendant Operator assisted call that Route Advanced.
4 = Call routed to Least Cost Routing.
5 = Attendant Operator assisted call that is routed to Least Cost Routing. |
| 056 | Selected Route – Hundredths | When Condition Code Three shows 2 through 5, this shows the selected route.
Otherwise this field blank. |
| 057 | Selected Route – Tenths | The tenth's place digit of the selected route number for the call |
| 058 | Selected Route – Ones | The one's digit of the first attempted route |
| 059 | First Route – Hundredths | When Condition Code Three shows 2 through 5, this shows the First Choice route. Otherwise this field blank.
If ASYD System 1, Index 32, Bit 2 = 0 then ARNP for the selected route will be in this field. If ARNP is set to * then ‘011’ will be here. If ARNP is set to # then ‘012’ will be here. |
| 060 | First Route – Tenths | The tenth's digit representing the first routing choice for the incoming call |
| 061 | First Route – Ones | The one's digit of the first attempted route |
| 062~085 | Called Number1 (max 24 digits) | If ASYD System 1, Index 32, Bit 5 = 1 then the dialed access code (i.e. 9) is included.
When ASYD System 1, Index 32, Bit 6 =
0 – Digits sent are in this field (after AOPR, AADT, etc.)
1 – Digits dialed are in this field (except access code)
When ARTD CDN 121 =
0 – Digits sent are in this field (after AOPR, AADT, etc.)
1 – Digits dialed are in this field (except the access code)
Note: ARTD overrides ASYD. |
| 086~093 | Not Used | Not Used |
| 094 | Metering Pulse – Thousands | When Metering Pulses are received from C.O., they will be in this field. If there is no information, these fields will be set to ‘0’. |
| 095 | Metering Pulse – Hundredths | When Metering Pulses are received from C.O., they will be in this field. If there is no information, these fields will be set to ‘0’. |
| 096 | Metering Pulse – Tenths | When Metering Pulses are received from C.O., they will be in this field. If there is no information, these fields will be set to ‘0’. |
| 097 | Metering Pulse – Ones | When Metering Pulses are received from C.O., they will be in this field. If there is no information, these fields will be set to ‘0’. |
| 098 | Office Code 1 (Digit 1) | CCIS Office Code from ARNP Route 0 in the Originating PBX. When ASYD Index 186 Bit 7 = 1 |
| 099 | Office Code 1 (Digit 2) | CCIS Office Code from ARNP Route 0 in the Originating PBX. When ASYD Index 186 Bit 7 = 2 |
| 100 | Office Code 1 (Digit 3) | CCIS Office Code from ARNP Route 0 in the Originating PBX. When ASYD Index 186 Bit 7 = 3 |
| 101 | Office Code 1 (Digit 4) | CCIS Office Code from ARNP Route 0 in the Originating PBX. When ASYD Index 186 Bit 7 = 4 |
| 102 | Office Code 2 (Digit 1) | CCIS Office Code from ARNP Route 0 in the Billing PBX (PBX that created the SMDR record). When ASYD Index 186 Bit 7 = 1 |
| 103 | Office Code 2 (Digit 2) | CCIS Office Code from ARNP Route 0 in the Billing PBX (PBX that created the SMDR record). When ASYD Index 186 Bit 7 = 2 |
| 104 | Office Code 2 (Digit 3) | CCIS Office Code from ARNP Route 0 in the Billing PBX (PBX that created the SMDR record). When ASYD Index 186 Bit 7 = 3 |
| 105 | Office Code 2 (Digit 4) | CCIS Office Code from ARNP Route 0 in the Billing PBX (PBX that created the SMDR record). When ASYD Index 186 Bit 7 = 4 |
| 106~115 | Authorization Code | Procedure 2 Auth Code Only
Max digits effected by ASYD Index 435; Bit 6 = 0 : Max 8 digits
Bit 6 = 1 : Max 10 digits |
| 116 | Year – Tenths | Year of start of conversation |
| 117 | Year – Ones | Year of start of conversation |
| 118 | Year – Tenths | Year of end of conversation
(Year included starting in 5200 (HDS) software) |
| 119 | Year – Ones | Year of end of conversation
(Year included starting in 5200 (HDS) software) |
| 120 | ISDN Advise of Charge Charge Condition Codes (Basic Unit of charge) | 0 = No data
1 = Charge information for 0.1 cent unit
2 = Charge information for 1 cent unit
3 = Charge information for 10 cent unit
4 = Charge information for 1 dollar unit 5~E = Not used
F = Charge information error (the maximum value is exceeded) |
| 121 | Charge (Basic Unit x 105) | ISDN Charge Information
See feature A-91 “Advice Of Charge SMDR” in the ISDN manual for detailed information. |
| 122 | Charge (Basic Unit x 104) | ISDN Charge Information
See feature A-91 “Advice Of Charge SMDR” in the ISDN manual for detailed information. |
| 123 | Charge (Basic Unit x 103) | ISDN Charge Information
See feature A-91 “Advice Of Charge SMDR” in the ISDN manual for detailed information. |
| 124 | Charge (Basic Unit x 102) | ISDN Charge Information
See feature A-91 “Advice Of Charge SMDR” in the ISDN manual for detailed information. |
| 125 | Charge (Basic Unit x 10) | ISDN Charge Information
See feature A-91 “Advice Of Charge SMDR” in the ISDN manual for detailed information. |
| 126 | Charge (Basic Unit) | ISDN Charge Information
See feature A-91 “Advice Of Charge SMDR” in the ISDN manual for detailed information. |
| 127 | ATT Billing Report Indication | Indicates the inclusion of a call in AT&T billing |
| 128~130 | Billing Report ATT Number | A unique number assigned to this call for AT&T billing purposes |
| 131 | ETX | End of Text |

---

## KB RECORD

**Description:** The KB SMDR Record provides information for station-to-station calls in a normal format of 131 characters, detailing the calling party's identity, the call duration, and the called party's number.

| CHARACTER | SMDR FIELD NAME AND DESCRIPTION | SMDR FIELD NAME COMMENT |
|---------------------------|----------------------------------|-------------------------|
| 000 | STX | Start of Text |
| 001 | SA | System Address; fixed data |
| 002 | UA | Unit Address |
| 003 | Entry Index “K” | “K” = SMDR record |
| 004 | Type of Record “B” | “B” = Station to Station / Normal Format |
| 005 | Blank | nan |
| 006 | Blank | nan |
| 007 | Blank | nan |
| 008 | Blank | nan |
| 009 | Blank | nan |
| 010 | Blank | nan |
| 011 | Calling Party Identification | 0 = PBX/CTX (DID) station
1 = Attendant Console |
| 012 | Tenant – 1st digit | Only in 1000 & 2000 (RDS) Feature Packages. 3000 (RDS) and above, fields are blank. |
| 013 | Tenant – 2nd digit | Reflects the second digit of a tenant's identifier |
| 014 | Calling Number – 1 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 011 is;
0 – Station number is shown
1 – Attendant number is shown |
| 015 | Calling Number – 2 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 011 is;
0 – Station number is shown
1 – Attendant number is shown |
| 016 | Calling Number – 3 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 011 is;
0 – Station number is shown
1 – Attendant number is shown |
| 017 | Calling Number – 4 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 011 is;
0 – Station number is shown
1 – Attendant number is shown |
| 018 | Calling Number – 5 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 011 is;
0 – Station number is shown
1 – Attendant number is shown |
| 019 | Calling Number – 6 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 011 is;
0 – Station number is shown
1 – Attendant number is shown |
| 020 | Month – Tenths | Time when SMDR record begins
For Station-To-Station this time begins when called party answers. |
| 021 | Month – Ones | Time when SMDR record begins
For Station-To-Station this time begins when called party answers. |
| 022 | Day – Tenths | Time when SMDR record begins
For Station-To-Station this time begins when called party answers. |
| 023 | Day – Ones | Time when SMDR record begins
For Station-To-Station this time begins when called party answers. |
| 024 | Hour – Tenths | Time when SMDR record begins
For Station-To-Station this time begins when called party answers. |
| 025 | Hour – Ones | Time when SMDR record begins
For Station-To-Station this time begins when called party answers. |
| 026 | Minute – Tenths | Time when SMDR record begins
For Station-To-Station this time begins when called party answers. |
| 027 | Minute – Ones | Time when SMDR record begins
For Station-To-Station this time begins when called party answers. |
| 028 | Second – Tenths | Time when SMDR record begins
For Station-To-Station this time begins when called party answers. |
| 029 | Second – Ones | Time when SMDR record begins
For Station-To-Station this time begins when called party answers. |
| 030 | Month –Tenths | Time when SMDR record is complete |
| 031 | Month – Ones | Time when SMDR record is complete |
| 032 | Day – Tenths | Time when SMDR record is complete |
| 033 | Day – Ones | Time when SMDR record is complete |
| 034 | Hour – Tenths | Time when SMDR record is complete |
| 035 | Hour – Ones | Time when SMDR record is complete |
| 036 | Minute – Tenths | Time when SMDR record is complete |
| 037 | Minute – Ones | Time when SMDR record is complete |
| 038 | Second – Tenths | Time when SMDR record is complete |
| 039 | Second – Ones | Time when SMDR record is complete |
| 040~049 | Account Code (max 10 digits) | Blank if Account Code not present |
| 050 | Tenant – 1st digit | Calling Party Tenant Information
This is for 3000 (RDS) Series Feature Package and higher. |
| 051 | Tenant – 2nd digit | Reflects the second digit of a tenant's identifier |
| 052 | Tenant – 3rd digit | Reflects the third digit of a tenant's identifier |
| 053 | Condition Code One | 0 = Call has not transferred
1 = Call has been transferred
Example:
Station-A calls Station-B, talks for 10 minutes then transfers outside to Station-C. The SMDR record will show Condition 1.
(Note: ASYD System 1 Index 33 will effect who is billed on a transfer) |
| 054 | Condition Code Two | Set to ‘0’ |
| 055 | Condition Code Three | 0 = Regular Outgoing or Tandem call.
1 = Attendant Operator assisted call. |
| 056~061 | Route Advance | Normally Blank |
| 062 | Called Tenant – 1st digit | Only in 1000 & 2000 (RDS) Feature Packages. 3000 (RDS) and above, fields are blank. |
| 063 | Called Tenant – 2nd digit | The second digit of the called party's tenant code |
| 064 | Called Number – 1 | Station number that was called. |
| 065 | Called Number – 2 | Station number that was called. |
| 066 | Called Number – 3 | Station number that was called. |
| 067 | Called Number – 4 | Station number that was called. |
| 068 | Called Number – 5 | Station number that was called. |
| 069 | Called Number – 6 | Station number that was called. |
| 070 | Called Tenant – 1st digit | Called Party Tenant Information
This is for 3000 (RDS) Series Feature Package and higher. |
| 071 | Called Tenant – 2nd digit | Called Party Tenant Information
This is for 3000 (RDS) Series Feature Package and higher. |
| 072 | Called Tenant – 3rd digit | Called Party Tenant Information
This is for 3000 (RDS) Series Feature Package and higher. |
| 073~093 | Blank | nan |
| 094~097 | 0 | All set to ‘0’ |
| 098~115 | Blank | nan |
| 116 | Year – Tenths | Year of start of conversation |
| 117 | Year – Ones | Year of start of conversation |
| 118 | Year – Tenths | Year of end of conversation
(Year included starting in 5200 (HDS) software) |
| 119 | Year – Ones | Year of end of conversation
(Year included starting in 5200 (HDS) software) |
| 120~130 | Blank | nan |
| 131 | ETX | End of Text |

---

## KE RECORD

**Description:** The KE SMDR Record captures detailed information for incoming calls in a standard 131-character format, including the route and trunk, identity of the called party, call duration, account and authorization codes, called party number, metering pulses, and ISDN charge information.

| CHARACTER | SMDR FIELD NAME AND DESCRIPTION | SMDR FIELD NAME COMMENT |
|---------------------------|----------------------------------|-------------------------|
| 000 | STX | Start of Text |
| 001 | SA | System Address; fixed data |
| 002 | UA | Unit Address |
| 003 | Entry Index “K” | “K” = SMDR record |
| 004 | Type of Record “E” | “E” = Incoming Call / Normal Format |
| 005 | Route Number – Hundredths | Incoming Route and Trunk information |
| 006 | Route Number – Tenths | Incoming Route and Trunk information |
| 007 | Route Number – Ones | Incoming Route and Trunk information |
| 008 | Trunk Number – Hundredths | Incoming Route and Trunk information |
| 009 | Trunk Number – Tenths | Incoming Route and Trunk information |
| 010 | Trunk Number – Ones | Incoming Route and Trunk information |
| 011 | Called Party Identification | 0 = PBX/CTX (DID) station
1 = Attendant Console
2 = Incoming Trunk |
| 012 | Tenant – 1st digit | Only in 1000 & 2000 (RDS) Feature Packages. 3000 (RDS) and above, fields are blank. |
| 013 | Tenant – 2nd digit | Only in 1000 & 2000 (RDS) Feature Packages. 3000 (RDS) and above, fields are blank. |
| 014 | Called Number – 1 | Information shown in Called Number fields depends on the Called Party Identification. When character 011 is;
0 – Station number is shown
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 015 | Called Number – 2 | Information shown in Called Number fields depends on the Called Party Identification. When character 011 is;
0 – Station number is shown
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 016 | Called Number – 3 | Information shown in Called Number fields depends on the Called Party Identification. When character 011 is;
0 – Station number is shown
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 017 | Called Number – 4 | Information shown in Called Number fields depends on the Called Party Identification. When character 011 is;
0 – Station number is shown
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 018 | Called Number – 5 | Information shown in Called Number fields depends on the Called Party Identification. When character 011 is;
0 – Station number is shown
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 019 | Called Number – 6 | Information shown in Called Number fields depends on the Called Party Identification. When character 011 is;
0 – Station number is shown
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 020 | Month – Tenths | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 021 | Month – Ones | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 022 | Day – Tenths | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 023 | Day – Ones | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 024 | Hour – Tenths | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 025 | Hour – Ones | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 026 | Minute – Tenths | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 027 | Minute – Ones | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 028 | Second – Tenths | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 029 | Second – Ones | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 030 | Month –Tenths | Time when SMDR record is complete |
| 031 | Month – Ones | Time when SMDR record is complete |
| 032 | Day – Tenths | Time when SMDR record is complete |
| 033 | Day – Ones | Time when SMDR record is complete |
| 034 | Hour – Tenths | Time when SMDR record is complete |
| 035 | Hour – Ones | Time when SMDR record is complete |
| 036 | Minute – Tenths | Time when SMDR record is complete |
| 037 | Minute – Ones | Time when SMDR record is complete |
| 038 | Second – Tenths | Time when SMDR record is complete |
| 039 | Second – Ones | Time when SMDR record is complete |
| 040~049 | Account Code (max 10 digits) | Blank if Account Code not present |
| 050 | Tenant – 1st digit | Called Party Tenant Information
This is for 3000 (RDS) Series Feature Package and higher. |
| 051 | Tenant – 2nd digit | Called Party Tenant Information
This is for 3000 (RDS) Series Feature Package and higher. |
| 052 | Tenant – 3rd digit | Called Party Tenant Information
This is for 3000 (RDS) Series Feature Package and higher. |
| 053 | Condition Code One | 0 = Call has not transferred
1 = Call has been transferred Example:
Station-A calls Station-B, talks for 10 minutes then transfers outside to Station-C. The SMDR record will show Condition 1.
(Note: ASYD System 1 Index 33 will effect who is billed on a transfer) |
| 054 | Condition Code Two | 0 = Incoming, Outgoing, or Tandem call with neither Outgoing Trunk Queuing nor Account Codes used.
1 = Outgoing Trunk Queuing used, but not Account Codes.
2 = Account Codes used, but not Outgoing Trunk Queuing.
3 = Both Outgoing Trunk Queuing and Account Codes used. |
| 055 | Condition Code Three | 0 = Regular Outgoing or Tandem call.
1 = Attendant Operator assisted call.
2 = The call Route Advanced (AOPR).
3 = Attendant Operator assisted call that Route Advanced.
4 = Call routed to Least Cost Routing.
5 = Attendant Operator assisted call that is routed to Least Cost Routing. |
| 056 | Selected Route – Hundredths | When Condition Code Three shows 2 through 5, this shows the selected route.
Otherwise this field blank. |
| 057 | Selected Route – Tenths | When Condition Code Three shows 2 through 5, this shows the selected route.
Otherwise this field blank. |
| 058 | Selected Route – Ones | When Condition Code Three shows 2 through 5, this shows the selected route.
Otherwise this field blank. |
| 059 | First Route – Hundredths | When Condition Code Three shows 2 through 5, this shows the First Choice route. Otherwise this field blank.
If ASYD System 1, Index 32, Bit 2 = 0 then ARNP for the selected route will be in this field. If ARNP is set to * then ‘011’ will be here. If ARNP is set to # then ‘012’ will be here. |
| 060 | First Route – Tenths | When Condition Code Three shows 2 through 5, this shows the First Choice route. Otherwise this field blank.
If ASYD System 1, Index 32, Bit 2 = 0 then ARNP for the selected route will be in this field. If ARNP is set to * then ‘011’ will be here. If ARNP is set to # then ‘012’ will be here. |
| 061 | First Route – Ones | When Condition Code Three shows 2 through 5, this shows the First Choice route. Otherwise this field blank.
If ASYD System 1, Index 32, Bit 2 = 0 then ARNP for the selected route will be in this field. If ARNP is set to * then ‘011’ will be here. If ARNP is set to # then ‘012’ will be here. |
| 062~085 | Called Number (max 24 digits) | If ASYD System 1, Index 32, Bit 5 = 1 then the dialed access code (i.e. 9) is included.
When ASYD System 1, Index 32, Bit 6 =
0 – Digits sent are in this field (after AOPR, AADT, etc.)
1 – Digits dialed are in this field (except access code)
When ARTD CDN 121 =
0 – Digits sent are in this field (after AOPR, AADT, etc.)
1 – Digits dialed are in this field (except the access code)
Note: ARTD overrides ASYD. |
| 086~093 | Not Used | Not Used |
| 094 | Metering Pulse – Thousands | When Metering Pulses are received from C.O., they will be in this field. If there is no information, these fields will be set to ‘0’. |
| 095 | Metering Pulse – Hundredths | When Metering Pulses are received from C.O., they will be in this field. If there is no information, these fields will be set to ‘0’. |
| 096 | Metering Pulse – Tenths | When Metering Pulses are received from C.O., they will be in this field. If there is no information, these fields will be set to ‘0’. |
| 097 | Metering Pulse – Ones | When Metering Pulses are received from C.O., they will be in this field. If there is no information, these fields will be set to ‘0’. |
| 098 | Office Code 1 (Digit 1) | CCIS Office Code from ARNP Route 0 in the Originating PBX. When ASYD Index 186 Bit 7 = 1 |
| 099 | Office Code 1 (Digit 2) | Fields 98~115 can display either the CCIS Office Code or ISDN Caller ID depending on the setting of
ASYD Index 186 Bit 7. |
| 100 | Office Code 1 (Digit 3) | CCIS Office Code from ARNP Route 0 in the Originating
PBX. When ASYD Index 186 Bit 7 = 1 |
| 101 | Office Code 1 (Digit 4) | CCIS Office Code from ARNP Route 0 in the Originating
PBX. When ASYD Index 186 Bit 7 = 1 |
| 102 | Office Code 2 (Digit 1) | CCIS Office Code from ARNP Route 0 in the Billing PBX
(PBX that created the SMDR record). When ASYD
Index 186 Bit 7 = 1 |
| 103 | Office Code 2 (Digit 2) | CCIS Office Code from ARNP Route 0 in the Billing PBX
(PBX that created the SMDR record). When ASYD
Index 186 Bit 7 = 1 |
| 104 | Office Code 2 (Digit 3) | CCIS Office Code from ARNP Route 0 in the Billing PBX
(PBX that created the SMDR record). When ASYD
Index 186 Bit 7 = 1 |
| 105 | Office Code 2 (Digit 4) | CCIS Office Code from ARNP Route 0 in the Billing PBX
(PBX that created the SMDR record). When ASYD
Index 186 Bit 7 = 1 |
| 098~1151 | ISDN Calling Party Number2 | When ASYD Index 241 Bit 4 = 1, the incoming ISDN Caller ID will be in these fields and not the CCIS Office Code.
1 Fields 98~115 can display either the CCIS Office Code or ISDN Caller ID depending on the setting of ASYD Index 186 Bit 7.
2 If ACND/N & ACNP/N are used to add digits (such as the Trunk Access Code), they will appear in this
field. |
| 116 | Year – Tenths | Year of start of conversation |
| 117 | Year – Ones | The one's digit of the year |
| 118 | Year – Tenths | Year of end of conversation
(Year included starting in 5200 (HDS) software) |
| 119 | Year – Ones | The one's digit of the year |
| 120 | ISDN Advise of Charge Charge Condition Codes (Basic Unit of charge) | 0 = No data
1 = Charge information for 0.1 cent unit
2 = Charge information for 1 cent unit
3 = Charge information for 10 cent unit
4 = Charge information for 1 dollar unit 5~E = Not used
F = Charge information error (the maximum value is exceeded) |
| 121 | Charge (Basic Unit x 105) | ISDN Charge Information
See feature A-91 “Advice Of Charge SMDR” in the ISDN manual for detailed information. |
| 122 | Charge (Basic Unit x 104) | ISDN Charge Information
See feature A-91 “Advice Of Charge SMDR” in the ISDN manual for detailed information. |
| 123 | Charge (Basic Unit x 103) | ISDN Charge Information
See feature A-91 “Advice Of Charge SMDR” in the ISDN manual for detailed information. |
| 124 | Charge (Basic Unit x 102) | ISDN Charge Information
See feature A-91 “Advice Of Charge SMDR” in the ISDN manual for detailed information. |
| 125 | Charge (Basic Unit x 10) | ISDN Charge Information
See feature A-91 “Advice Of Charge SMDR” in the ISDN manual for detailed information. |
| 126 | Charge (Basic Unit) | ISDN Charge Information
See feature A-91 “Advice Of Charge SMDR” in the ISDN manual for detailed information. |
| 127 | ATT Billing Report Indication | Indicates the inclusion of a call in AT&T billing |
| 128~130 | Billing Report ATT Number | A unique number assigned to this call for AT&T billing purposes |
| 131 | ETX | End of Text |

---

## KH RECORD

**Description:** The KE SMDR Record captures detailed information for incoming calls in a standard 131-character format, including the route and trunk, identity of the called party, call duration, account and authorization codes, called party number, metering pulses, and ISDN charge information.

| CHARACTER | SMDR FIELD NAME AND DESCRIPTION | SMDR FIELD NAME COMMENT |
|---------------------------|----------------------------------|-------------------------|
| 000 | STX | Start of Text |
| 001 | 0 | System Address; fixed data |
| 002 | ! | Unit Address |
| 003 | Entry Index “K” | “K” = SMDR record |
| 004 | Type of Record “H” | “H” = Outgoing Call / Extended Format |
| 005 | Route Number – Hundredths | Outgoing Route and Trunk information |
| 006 | Route Number – Tenths | Outgoing Route and Trunk information |
| 007 | Route Number – Ones | Outgoing Route and Trunk information |
| 008 | Trunk Number – Hundredths | Outgoing Route and Trunk information |
| 009 | Trunk Number – Tenths | Outgoing Route and Trunk information |
| 010 | Trunk Number – Ones | Outgoing Route and Trunk information |
| 011 | Calling Party Identification | 0 = PBX/CTX (DID) station
1 = Attendant Console
2 = Incoming Trunk
3 = Monitored Number (See Appendix D) |
| 012 | Tenant – 1st digit | Only in 1000 & 2000 (RDS) Feature Packages. 3000 (RDS) and above, fields are blank. |
| 013 | Tenant – 2nd digit | Only in 1000 & 2000 (RDS) Feature Packages. 3000 (RDS) and above, fields are blank. |
| 014 | Calling Number – 1 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 011 is;
0 – Station number is shown1
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 015 | Calling Number – 2 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 011 is; 0 – Station number is shown1 1 – Attendant number is shown 2 – 3 digit Route and Trunk number |
| 016 | Calling Number – 3 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 011 is; 0 – Station number is shown1 1 – Attendant number is shown 2 – 3 digit Route and Trunk number |
| 017 | Calling Number – 4 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 011 is; 0 – Station number is shown1 1 – Attendant number is shown 2 – 3 digit Route and Trunk number
1 If tandem from ISDN, ASYD 241 bit 6 effects what is displayed (first or last digits)1 If tandem from ISDN, ASYD 241 bit 6 effects what is displayed (first or last digits) |
| 018 | Calling Number – 5 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 011 is; 0 – Station number is shown1 1 – Attendant number is shown 2 – 3 digit Route and Trunk number |
| 019 | Calling Number – 6 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 011 is; 0 – Station number is shown1 1 – Attendant number is shown 2 – 3 digit Route and Trunk number |
| 020 | Month – Tenths | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is effected by ARTD CDN28 or ASYD Index 156 & 157. |
| 021 | Month – Ones | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is effected by ARTD CDN28 or ASYD Index 156 & 157. |
| 022 | Day – Tenths | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is effected by ARTD CDN28 or ASYD Index 156 & 157. |
| 023 | Day – Ones | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is effected by ARTD CDN28 or ASYD Index 156 & 157. |
| 024 | Hour – Tenths | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is effected by ARTD CDN28 or ASYD Index 156 & 157. |
| 025 | Hour – Ones | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is effected by ARTD CDN28 or ASYD Index 156 & 157. |
| 026 | Minute – Tenths | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is effected by ARTD CDN28 or ASYD Index 156 & 157. |
| 027 | Minute – Ones | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is effected by ARTD CDN28 or ASYD Index 156 & 157. |
| 028 | Second – Tenths | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is effected by ARTD CDN28 or ASYD Index 156 & 157. |
| 029 | Second – Ones | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is effected by ARTD CDN28 or ASYD Index 156 & 157. |
| 030 | Month –Tenths | Time when SMDR record is complete |
| 031 | Month – Ones | Time when SMDR record is complete |
| 032 | Day – Tenths | Time when SMDR record is complete |
| 033 | Day – Ones | Time when SMDR record is complete |
| 034 | Hour – Tenths | Time when SMDR record is complete |
| 035 | Hour – Ones | Time when SMDR record is complete |
| 036 | Minute – Tenths | Time when SMDR record is complete |
| 037 | Minute – Ones | Time when SMDR record is complete |
| 038 | Second – Tenths | Time when SMDR record is complete |
| 039 | Second – Ones | Time when SMDR record is complete |
| 040~049 | Account Code (max 10 digits) | Blank if Account Code not present |
| 050 | Tenant – 1st digit | Calling Party Tenant Information
This is for 3000 (RDS) Series Feature Package and higher. |
| 051 | Tenant – 2nd digit | Calling Party Tenant Information
This is for 3000 (RDS) Series Feature Package and higher. |
| 052 | Tenant – 3rd digit | Calling Party Tenant Information
This is for 3000 (RDS) Series Feature Package and higher. |
| 1 If tandem from ISDN, ASYD 241 bit 6 effects what is displayed (first or last digits) | nan | nan |
| 053 | Condition Code One | 0 = Call has not transferred
1 = Call has been transferred Example:
Station-A calls Station-B, talks for 10 minutes then transfers outside to Station-C. The SMDR record will show Condition 1.
(Note: ASYD System 1 Index 33 will effect who is billed on a transfer) |
| 054 | Condition Code Two | 0 = Incoming, Outgoing, or Tandem call with neither Outgoing Trunk Queuing nor Account Codes used.
1 = Outgoing Trunk Queuing used, but not Account Codes.
2 = Account Codes used, but not Outgoing Trunk Queuing.
3 = Both Outgoing Trunk Queuing and Account Codes used. |
| 055 | Condition Code Three | 0 = Regular Outgoing or Tandem call.
1 = Attendant Operator assisted call.
2 = The call Route Advanced (AOPR).
3 = Attendant Operator assisted call that Route Advanced.
4 = Call routed to Least Cost Routing.
5 = Attendant Operator assisted call that is routed to Least Cost Routing. |
| 056 | Selected Route – Hundredths | When Condition Code Three shows 2 through 5, this shows the selected route.
Otherwise this field blank. |
| 057 | Selected Route – Tenths | When Condition Code Three shows 2 through 5, this shows the selected route.
Otherwise this field blank. |
| 058 | Selected Route – Ones | When Condition Code Three shows 2 through 5, this shows the selected route.
Otherwise this field blank. |
| 059 | First Route – Hundredths | When Condition Code Three shows 2 through 5, this shows the First Choice route. Otherwise this field blank.
If ASYD System 1, Index 32, Bit 2 = 0 then ARNP for the selected route will be in this field. If ARNP is set to * then ‘011’ will be here. If ARNP is set to # then ‘012’ will be here. |
| 060 | First Route – Tenths | When Condition Code Three shows 2 through 5, this shows the First Choice route. Otherwise this field blank.
If ASYD System 1, Index 32, Bit 2 = 0 then ARNP for the selected route will be in this field. If ARNP is set to * then ‘011’ will be here. If ARNP is set to # then ‘012’ will be here. |
| 061 | First Route – Ones | When Condition Code Three shows 2 through 5, this shows the First Choice route. Otherwise this field blank.
If ASYD System 1, Index 32, Bit 2 = 0 then ARNP for the selected route will be in this field. If ARNP is set to * then ‘011’ will be here. If ARNP is set to # then ‘012’ will be here. |
| 062~085 | Called Number1 (max 24 digits) | If ASYD System 1, Index 32, Bit 5 = 1 then the dialed access code (i.e. 9) is included.
When ASYD System 1, Index 32, Bit 6 =
0 – Digits sent are in this field (after AOPR, AADT, etc.)
1 – Digits dialed are in this field (except access code)
When ARTD CDN 121 =
0 – Digits sent are in this field (after AOPR, AADT, etc.)
1 – Digits dialed are in this field (except the access code)
Note: ARTD overrides ASYD. |
| 086~093 | Not Used | Not Used |
| 094 | Metering Pulse – Thousands | When Metering Pulses are received from C.O., they will be in this field. If there is no information, these fields will be set to ‘0’. |
| 095 | Metering Pulse – Hundredths | When Metering Pulses are received from C.O., they will be in this field. If there is no information, these fields will be set to ‘0’. |
| 096 | Metering Pulse – Tenths | When Metering Pulses are received from C.O., they will be in this field. If there is no information, these fields will be set to ‘0’. |
| 097 | Metering Pulse – Ones | When Metering Pulses are received from C.O., they will be in this field. If there is no information, these fields will be set to ‘0’. |
| 098 | Office Code 1 (Digit 1) | CCIS Office Code from ARNP Route 0 in the Originating PBX. When ASYD Index 186 Bit 7 = 1 |
| 099 | Office Code 1 (Digit 2) | CCIS Office Code from ARNP Route 0 in the Originating PBX. When ASYD Index 186 Bit 7 = 2 |
| 100 | Office Code 1 (Digit 3) | CCIS Office Code from ARNP Route 0 in the Originating PBX. When ASYD Index 186 Bit 7 = 3 |
| 101 | Office Code 1 (Digit 4) | CCIS Office Code from ARNP Route 0 in the Originating PBX. When ASYD Index 186 Bit 7 = 4 |
| 102 | Office Code 2 (Digit 1) | CCIS Office Code from ARNP Route 0 in the Billing PBX (where the call record was created). When ASYD Index 186 Bit 7 = 1 |
| 103 | Office Code 2 (Digit 2) | CCIS Office Code from ARNP Route 0 in the Billing PBX (where the call record was created). When ASYD Index 186 Bit 7 = 2 |
| 104 | Office Code 2 (Digit 3) | CCIS Office Code from ARNP Route 0 in the Billing PBX (where the call record was created). When ASYD Index 186 Bit 7 = 3 |
| 105 | Office Code 2 (Digit 4) | CCIS Office Code from ARNP Route 0 in the Billing PBX (where the call record was created). When ASYD Index 186 Bit 7 = 4 |
| 106~113 | Authorization Code | Procedure 2 Auth Code Only Max 8 digits |
| 114~115 | Blank | nan |
| 116 | Year – Tenths | Year of start of conversation |
| 117 | Year – Ones | Year of start of conversation |
| 118 | Year – Tenths | Year of end of conversation |
| 119 | Year – Ones | Year of end of conversation |
| 120 | ISDN Advise of Charge Charge Condition Codes (Basic Unit of charge) | 0 = No data
1 = Charge information for 0.1 cent unit
2 = Charge information for 1 cent unit
3 = Charge information for 10 cent unit
4 = Charge information for 1 dollar unit 5~E = Not used
F = Charge information error (the maximum value is exceeded) |
| 121 | Charge (Basic Unit x 105) | ISDN Charge Information
See feature A-91 “Advice Of Charge SMDR” in the ISDN manual for detailed information. |
| 122 | Charge (Basic Unit x 104) | ISDN Charge Information
See feature A-91 “Advice Of Charge SMDR” in the ISDN manual for detailed information. |
| 123 | Charge (Basic Unit x 103) | ISDN Charge Information
See feature A-91 “Advice Of Charge SMDR” in the ISDN manual for detailed information. |
| 124 | Charge (Basic Unit x 102) | ISDN Charge Information
See feature A-91 “Advice Of Charge SMDR” in the ISDN manual for detailed information. |
| 125 | Charge (Basic Unit x 10) | ISDN Charge Information
See feature A-91 “Advice Of Charge SMDR” in the ISDN manual for detailed information. |
| 126 | Charge (Basic Unit) | ISDN Charge Information
See feature A-91 “Advice Of Charge SMDR” in the ISDN manual for detailed information. |
| 127 | ATT Billing Report Indication | Indicates the inclusion of a call in AT&T billing |
| 128~130 | Billing Report ATT Number | A unique number assigned to this call for AT&T billing purposes |
| 131 | Data Identification | A = Calling Party Number or ANI information present |
| 132 | Calling Party Number or ANI Presentation Identifier | 0 = Calling Party Number or ANI is not present
1 = Displayed
2 = Calling Party Number or ANI present, presentation restricted
3 = Service is not available
4 = Origination from public pay phone1
5 = Service Condition |
| 133~164 | Calling Party Number or ANI | Max 32 digits |
| 165 | Z | End of SMDR information |
| 166 | ETX | End of Text |

---

## KI RECORD

**Description:** The KI SMDR Record, with an extended format for incoming calls, includes route and trunk info, callee identification, call duration, account and authorization codes, called number, metering, ISDN charge info, and the calling party number/ANI.

| CHARACTER | SMDR FIELD NAME AND DESCRIPTION | SMDR FIELD NAME COMMENT |
|---------------------------|----------------------------------|-------------------------|
| 000 | STX | Start of Text |
| 001 | SA | System Address; fixed data |
| 002 | UA | Unit Address |
| 003 | Entry Index “K” | “K” = SMDR record |
| 004 | Type of Record “E” | “I” = Incoming Call / Extended Format |
| 005 | Route Number – Hundredths | Incoming Route and Trunk information |
| 006 | Route Number – Tenths | Incoming Route and Trunk information |
| 007 | Route Number – Ones | Incoming Route and Trunk information |
| 008 | Trunk Number – Hundredths | Incoming Route and Trunk information |
| 009 | Trunk Number – Tenths | Incoming Route and Trunk information |
| 010 | Trunk Number – Ones | Incoming Route and Trunk information |
| 011 | Called Party Identification | 0 = PBX/CTX (DID) station
1 = Attendant Console
2 = Incoming Trunk |
| 012 | Tenant – 1st digit | Only in 1000 & 2000 (RDS) Feature Packages. 3000 (RDS) and above, fields are blank. |
| 013 | Tenant – 2nd digit | Only in 1000 & 2000 (RDS) Feature Packages. 3000 (RDS) and above, fields are blank. |
| 014 | Called Number – 1 | Information shown in Called Number fields depends on the Called Party Identification. When character 011 is;
0 – Station number is shown
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 015 | Called Number – 2 | Information shown in Called Number fields depends on the Called Party Identification. When character 011 is;
0 – Station number is shown
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 016 | Called Number – 3 | Information shown in Called Number fields depends on the Called Party Identification. When character 011 is;
0 – Station number is shown
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 017 | Called Number – 4 | Information shown in Called Number fields depends on the Called Party Identification. When character 011 is;
0 – Station number is shown
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 018 | Called Number – 5 | Information shown in Called Number fields depends on the Called Party Identification. When character 011 is;
0 – Station number is shown
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 019 | Called Number – 6 | Information shown in Called Number fields depends on the Called Party Identification. When character 011 is;
0 – Station number is shown
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 020 | Month – Tenths | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 021 | Month – Ones | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 022 | Day – Tenths | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 023 | Day – Ones | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 024 | Hour – Tenths | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 025 | Hour – Ones | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 026 | Minute – Tenths | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 027 | Minute – Ones | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 028 | Second – Tenths | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 029 | Second – Ones | Time when SMDR record begins
For Station-To-Route the SMDR record begins when Answer Supervision has taken place. This is affected by ARTD CDN28 or ASYD Index 156 & 157. |
| 030 | Month –Tenths | Time when SMDR record is complete |
| 031 | Month – Ones | Time when SMDR record is complete |
| 032 | Day – Tenths | Time when SMDR record is complete |
| 033 | Day – Ones | Time when SMDR record is complete |
| 034 | Hour – Tenths | Time when SMDR record is complete |
| 035 | Hour – Ones | Time when SMDR record is complete |
| 036 | Minute – Tenths | Time when SMDR record is complete |
| 037 | Minute – Ones | Time when SMDR record is complete |
| 038 | Second – Tenths | Time when SMDR record is complete |
| 039 | Second – Ones | Time when SMDR record is complete |
| 040~049 | Account Code (max 10 digits) | Blank if Account Code not present |
| 050 | Tenant – 1st digit | Called Party Tenant Information
This is for 3000 (RDS) Series Feature Package and higher. |
| 051 | Tenant – 2nd digit | Called Party Tenant Information
This is for 3000 (RDS) Series Feature Package and higher. |
| 052 | Tenant – 3rd digit | Called Party Tenant Information
This is for 3000 (RDS) Series Feature Package and higher. |
| 053 | Condition Code One | 0 = Call has not transferred
1 = Call has been transferred Example:
Station-A calls Station-B, talks for 10 minutes then transfers outside to Station-C. The SMDR record will show Condition 1.
(Note: ASYD System 1 Index 33 will effect who is billed on a transfer) |
| 054 | Condition Code Two | 0 = Incoming, Outgoing, or Tandem call with neither Outgoing Trunk Queuing nor Account Codes used.
1 = Outgoing Trunk Queuing used, but not Account Codes.
2 = Account Codes used, but not Outgoing Trunk Queuing.
3 = Both Outgoing Trunk Queuing and Account Codes used. |
| 055 | Condition Code Three | 0 = Regular Outgoing or Tandem call.
1 = Attendant Operator assisted call.
2 = The call Route Advanced (AOPR).
3 = Attendant Operator assisted call that Route Advanced.
4 = Call routed to Least Cost Routing.
5 = Attendant Operator assisted call that is routed to Least Cost Routing. |
| 056 | Selected Route – Hundredths | When Condition Code Three shows 2 through 5, this shows the selected route.
Otherwise this field blank. |
| 057 | Selected Route – Tenths | The Tenths place digit indicating the selected route for the incoming call. |
| 058 | Selected Route – Ones | The one's place digit indicating the selected route for the incoming call. |
| 059 | First Route – Hundredths | When Condition Code Three shows 2 through 5, this shows the First Choice route. Otherwise this field blank.
If ASYD System 1, Index 32, Bit 2 = 0 then ARNP for the selected route will be in this field. If ARNP is set to * then ‘011’ will be here. If ARNP is set to # then ‘012’ will be here. |
| 060 | First Route – Tenths | The tenth's digit representing the first routing choice for the incoming call |
| 061 | First Route – Ones | The one's digit of the first attempted route |
| 062~085 | Called Number (max 24 digits) | If ASYD System 1, Index 32, Bit 5 = 1 then the dialed access code (i.e. 9) is included.
When ASYD System 1, Index 32, Bit 6 =
0 – Digits sent are in this field (after AOPR, AADT, etc.)
1 – Digits dialed are in this field (except access code)
When ARTD CDN 121 =
0 – Digits sent are in this field (after AOPR, AADT, etc.)
1 – Digits dialed are in this field (except the access code)
Note: ARTD overrides ASYD. |
| 086~093 | Not Used | Not Used |
| 094 | Metering Pulse – Thousands | When Metering Pulses are received from C.O., they will be in this field. If there is no information, these fields will be set to ‘0’. |
| 095 | Metering Pulse – Hundredths | When Metering Pulses are received from C.O., they will be in this field. If there is no information, these fields will be set to ‘0’. |
| 096 | Metering Pulse – Tenths | When Metering Pulses are received from C.O., they will be in this field. If there is no information, these fields will be set to ‘0’. |
| 097 | Metering Pulse – Ones | When Metering Pulses are received from C.O., they will be in this field. If there is no information, these fields will be set to ‘0’. |
| 098 | Office Code 1 (Digit 1) | CCIS Office Code from ARNP Route 0 in the Originating PBX. When ASYD Index 186 Bit 7 = 1 |
| 099 | Office Code 1 (Digit 2) | CCIS Office Code from ARNP Route 0 in the Originating PBX. When ASYD Index 186 Bit 7 = 2 |
| 100 | Office Code 1 (Digit 3) | CCIS Office Code from ARNP Route 0 in the Originating PBX. When ASYD Index 186 Bit 7 = 3 |
| 101 | Office Code 1 (Digit 4) | CCIS Office Code from ARNP Route 0 in the Originating PBX. When ASYD Index 186 Bit 7 = 4 |
| 102 | Office Code 2 (Digit 1) | CCIS Office Code from ARNP Route 0 in the Billing PBX (PBX that created the SMDR record). When ASYD Index 186 Bit 7 = 1 |
| 103 | Office Code 2 (Digit 2) | CCIS Office Code from ARNP Route 0 in the Billing PBX (PBX that created the SMDR record). When ASYD Index 186 Bit 7 = 2 |
| 104 | Office Code 2 (Digit 3) | CCIS Office Code from ARNP Route 0 in the Billing PBX (PBX that created the SMDR record). When ASYD Index 186 Bit 7 = 3 |
| 105 | Office Code 2 (Digit 4) | CCIS Office Code from ARNP Route 0 in the Billing PBX (PBX that created the SMDR record). When ASYD Index 186 Bit 7 = 4 |
| 106~115 | Not Used | Not Used |
| 116 | Year – Tenths | Year of start of conversation |
| 117 | Year – Ones | Year of start of conversation |
| 118 | Year – Tenths | Year of end of conversation
(Year included starting in 5200 (HDS) software) |
| 119 | Year – Ones | Year of end of conversation
(Year included starting in 5200 (HDS) software) |
| 120 | ISDN Advise of Charge1 Charge Condition Codes (Basic Unit of charge) | 0 = No data
1 = Charge information for 0.1 cent unit
2 = Charge information for 1 cent unit
3 = Charge information for 10 cent unit
4 = Charge information for 1 dollar unit 5~E = Not used
F = Charge information error (the maximum value is exceeded) |
| 121 | Charge (Basic Unit x 105) | ISDN Charge Information
See feature A-91 “Advice Of Charge SMDR” in the ISDN manual for detailed information. |
| 122 | Charge (Basic Unit x 104) | ISDN Charge Information
See feature A-91 “Advice Of Charge SMDR” in the ISDN manual for detailed information. |
| 123 | Charge (Basic Unit x 103) | ISDN Charge Information
See feature A-91 “Advice Of Charge SMDR” in the ISDN manual for detailed information. |
| 124 | Charge (Basic Unit x 102) | ISDN Charge Information
See feature A-91 “Advice Of Charge SMDR” in the ISDN manual for detailed information. |
| 125 | Charge (Basic Unit x 10) | ISDN Charge Information
See feature A-91 “Advice Of Charge SMDR” in the ISDN manual for detailed information. |
| 126 | Charge (Basic Unit) | ISDN Charge Information
See feature A-91 “Advice Of Charge SMDR” in the ISDN manual for detailed information. |
| 127 | ATT Billing Report Indication | Indicates the inclusion of a call in AT&T billing |
| 128~130 | Billing Report ATT Number | A unique number assigned to this call for AT&T billing purposes |
| 131 | Calling Party Number or ANI | A = Calling Party Number or ANI information present |
| 132 | Calling Party Number or ANI Presentation Identifier | 0 = Calling Party Number or ANI is not present
1 = Displayed
2 = Calling Party Number or ANI present, presentation restricted
3 = Service is not available
4 = Origination from public pay phone2
5 = Service Condition |
| 133~161 | Calling Party Number or ANI3 | Max 32 digits |
| 165 | Z | End of SMDR information |
| 166 | ETX | End of Text |

---

## KJ RECORD

**Description:** The KJ SMDR Record is an extended format record for station-to-station calls, detailing caller identity, call duration, and the number of the called party.

| CHARACTER | SMDR FIELD NAME AND DESCRIPTION | SMDR FIELD NAME COMMENT |
|---------------------------|----------------------------------|-------------------------|
| 000 | STX | Start of Text |
| 001 | SA | System Address; fixed data |
| 002 | UA | Unit Address |
| 003 | Entry Index “K” | “K” = SMDR record |
| 004 | Type of Record “B” | “J” = Station to Station / Extended Format |
| 005 | Blank | For Station-To-Station calls, 005~010 are blank |
| 006 | Blank | nan |
| 007 | Blank | nan |
| 008 | Blank | nan |
| 009 | Blank | nan |
| 010 | Blank | nan |
| 011 | Calling Party Identification | 0 = PBX/CTX (DID) station
1 = Attendant Console |
| 012 | Tenant – 1st digit | Only in 1000 & 2000 (RDS) Feature Packages. 3000 (RDS) and above, fields are blank. |
| 013 | Tenant – 2nd digit | Reflects the second digit of a tenant's identifier |
| 014 | Calling Number – 1 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 011 is;
0 – Station number is shown
1 – Attendant number is shown |
| 015 | Calling Number – 2 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 011 is;
0 – Station number is shown
1 – Attendant number is shown |
| 016 | Calling Number – 3 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 011 is;
0 – Station number is shown
1 – Attendant number is shown |
| 017 | Calling Number – 4 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 011 is;
0 – Station number is shown
1 – Attendant number is shown |
| 018 | Calling Number – 5 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 011 is;
0 – Station number is shown
1 – Attendant number is shown |
| 019 | Calling Number – 6 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 011 is;
0 – Station number is shown
1 – Attendant number is shown |
| 020 | Month – Tenths | Time when SMDR record begins
For Station-To-Station this time begins when called party answers. |
| 021 | Month – Ones | Time when SMDR record begins
For Station-To-Station this time begins when called party answers. |
| 022 | Day – Tenths | Time when SMDR record begins
For Station-To-Station this time begins when called party answers. |
| 023 | Day – Ones | Time when SMDR record begins
For Station-To-Station this time begins when called party answers. |
| 024 | Hour – Tenths | Time when SMDR record begins
For Station-To-Station this time begins when called party answers. |
| 025 | Hour – Ones | Time when SMDR record begins
For Station-To-Station this time begins when called party answers. |
| 026 | Minute – Tenths | Time when SMDR record begins
For Station-To-Station this time begins when called party answers. |
| 027 | Minute – Ones | Time when SMDR record begins
For Station-To-Station this time begins when called party answers. |
| 028 | Second – Tenths | Time when SMDR record begins
For Station-To-Station this time begins when called party answers. |
| 029 | Second – Ones | Time when SMDR record begins
For Station-To-Station this time begins when called party answers. |
| 030 | Month –Tenths | Time when SMDR record is complete |
| 031 | Month – Ones | Time when SMDR record is complete |
| 032 | Day – Tenths | Time when SMDR record is complete |
| 033 | Day – Ones | Time when SMDR record is complete |
| 034 | Hour – Tenths | Time when SMDR record is complete |
| 035 | Hour – Ones | Time when SMDR record is complete |
| 036 | Minute – Tenths | Time when SMDR record is complete |
| 037 | Minute – Ones | Time when SMDR record is complete |
| 038 | Second – Tenths | Time when SMDR record is complete |
| 039 | Second – Ones | Time when SMDR record is complete |
| 040~049 | Account Code (max 10 digits) | Blank if Account Code not present |
| 050 | Tenant – 1st digit | Calling Party Tenant Information
This is for 3000 (RDS) Series Feature Package and higher. |
| 051 | Tenant – 2nd digit | Calling Party Tenant Information
This is for 3000 (RDS) Series Feature Package and higher. |
| 052 | Tenant – 3rd digit | Calling Party Tenant Information
This is for 3000 (RDS) Series Feature Package and higher. |
| 053 | Condition Code One | 0 = Call has not transferred
1 = Call has been transferred
Example:
Station-A calls Station-B, talks for 10 minutes then transfers outside to Station-C. The SMDR record will show Condition 1.
(Note: ASYD System 1 Index 33 will effect who is billed on a transfer) |
| 054 | Condition Code Two | Set to ‘0’ |
| 055 | Condition Code Three | 0 = Regular Outgoing or Tandem call.
1 = Attendant Operator assisted call. |
| 056~061 | Route Advance | Normally Blank |
| 062 | Called Tenant – 1st digit | Only in 1000 & 2000 (RDS) Feature Packages. 3000 (RDS) and above, fields are blank. |
| 063 | Called Tenant – 2nd digit | The second digit of the called party's tenant code |
| 064 | Called Number – 1 | Station number that was called. |
| 065 | Called Number – 2 | Station number that was called. |
| 066 | Called Number – 3 | Station number that was called. |
| 067 | Called Number – 4 | Station number that was called. |
| 068 | Called Number – 5 | Station number that was called. |
| 069 | Called Number – 6 | Station number that was called. |
| 070 | Called Tenant – 1st digit | Called Party Tenant Information
This is for 3000 (RDS) Series Feature Package and higher. |
| 071 | Called Tenant – 2nd digit | Called Party Tenant Information
This is for 3000 (RDS) Series Feature Package and higher. |
| 072 | Called Tenant – 3rd digit | Called Party Tenant Information
This is for 3000 (RDS) Series Feature Package and higher. |
| 073~093 | Blank | nan |
| 094~097 | 0 | All set to ‘0’ |
| 098~115 | Blank | nan |
| 116 | Year – Tenths | Year of start of conversation |
| 117 | Year – Ones | Year of start of conversation |
| 118 | Year – Tenths | Year of end of conversation
(Year included starting in 5200 (HDS) software) |
| 119 | Year – Ones | The one's digit of the year |
| 120~130 | Blank | nan |
| 131 | Calling Party Number / ANI | A = Calling Party Number / ANI Information Present |
| 132 | 0 | Set to ‘0’ |
| 133~164 | Blank | nan |
| 165 | Z | End of SMDR information |
| 166 | ETX | End of Text |

---

## KK RECORD

**Description:** The KK SMDR Record employs a flexible format to optimize data efficiency by removing data gaps. It uses indexes to describe the data and its length, adapting to varying content sizes instead of fixed byte allocations.

| CHARACTER | SMDR FIELD NAME AND DESCRIPTION | SMDR FIELD NAME COMMENT |
|---------------------------|----------------------------------|-------------------------|
| 01 | Outgoing Trunk / Incoming Trunk information | Indicates the trunk through which the call was routed |
| 02 | Calling Party Information (Physical Number) | Identifies the physical hardware number of the calling device |
| 03† | Calling Party Information (Telephone Number) | Reflects the actual telephone number of the caller |
| 06 | Call Start Time / Call End Time | Records the timestamps for the initiation and conclusion of the call |
| 07† | Account Code | Provides an account code associated with the call |
| 08 | Condition B Information | Contains specific condition codes that may affect how the call is handled |
| 09 | Alternate Routing Information / Incoming Route Number | Provides alternate routing details or the incoming route number for the call |
| 10 | Dial Code | Stores the dial code used for the call |
| 11† | Office Code Information | Captures the office code |
| 12† | Authorization Code | Records an authorization code |
| 13 | Condition C Information & Billing Information / Call Metering Information | Details condition C codes and related billing data |
| 14† | Condition D Information & Billing Notification AttCon Number | Includes condition D information and AttCon (Attendance Control) numbers for billing notifications |
| 15† | Department Code | Signifies the department code involved in the call |
| 16 | Calling Station Number | Identifies the calling station's number |
| 17† | Converted Number | Shows any converted number information |
| 18† | MA-ID (Multi Area ID) R15 software and above | Displays the MA-ID's one's digit |
| 000 | STX | Start of Text |
| 001 | 0 | System Address; fixed data |
| 002 | ! | Unit Address |
| 003 | Entry Index “K” | “K” = SMDR record |
| 004 | Type of Record “K” | “K” = Outgoing Call / Flexible Format |
| 001 | 0 | Kind of Data : 01 Outgoing Trunk |
| 002 | 1 | Kind of Data : 01 Outgoing Trunk |
| 003 | 1 | Length of Data = 12 characters |
| 004 | 2 | Length of Data = 12 characters |
| 005 | FPC – Hundredths | Seized Fusion Point Code |
| 006 | FPC – Tenths | Seized Fusion Point Code |
| 007 | FPC – Ones | Seized Fusion Point Code |
| 008 | Physical Route – Hundredths | Physical Outgoing Route Number (ARTD) |
| 009 | Physical Route – Tenths | Physical Outgoing Route Number (ARTD) |
| 010 | Physical Route – Ones | Physical Outgoing Route Number (ARTD) |
| 011 | Trunk – Hundredths | Trunk Number |
| 012 | Trunk – Tenths | Trunk Number |
| 013 | Trunk – Ones | Trunk Number |
| 014 | Logical Route – Hundredths | Logical Outgoing Route (ALRTN) if applicable |
| 015 | Logical Route – Tenths | Logical Outgoing Route (ALRTN) if applicable |
| 016 | Logical Route – Ones | Logical Outgoing Route (ALRTN) if applicable |
| 001 | 0 | Kind of Data : 02 Calling Party Information (Physical number) |
| 002 | 2 | Kind of Data : 02 Calling Party Information (Physical number) |
| 003 | 1 | Length of Data = 10 characters |
| 004 | 0 | Length of Data = 10 characters |
| 005 | Calling Party Identification | 0 = PBX/CTX (DID) station
1 = Attendant Console
2 = Incoming Trunk
3 = Monitored Number (See Appendix D) |
| 006 | Tenant – 1st digit | Calling Party Tenant |
| 007 | Tenant – 2nd digit | Calling Party Tenant |
| 008 | Tenant – 3rd digit | Calling Party Tenant |
| 009 | Calling Number – 1 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 005 is;
0 – Station number is shown1
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 010 | Calling Number – 2 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 005 is;
0 – Station number is shown1
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 011 | Calling Number – 3 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 005 is;
0 – Station number is shown1
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 012 | Calling Number – 4 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 005 is;
0 – Station number is shown1
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 013 | Calling Number – 5 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 005 is;
0 – Station number is shown1
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 014 | Calling Number – 6 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 005 is;
0 – Station number is shown1
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 001 | 0 | Kind of Data : 03 Calling Party Number (Telephone Number or Logical Route) |
| 002 | 3 | Kind of Data : 03 Calling Party Number (Telephone Number or Logical Route) |
| 003 | nan | Length of Data : Variable 3 to 22
03 when no data 22 maximum |
| 004 | nan | Length of Data : Variable 3 to 22
03 when no data 22 maximum |
| 005 | FPC – Hundredths | Fusion Point Code of Calling Party : If no Fusion Point Code present then these fields will be set to ‘0’ |
| 006 | FPC – Tenths | Fusion Point Code of Calling Party : If no Fusion Point Code present then these fields will be set to ‘0’ |
| 007 | FPC – Ones | Fusion Point Code of Calling Party : If no Fusion Point Code present then these fields will be set to ‘0’ |
| 008 | User Group – Hundredths | Fusion User Group Number of Calling Party |
| 009 | User Group – Tenths | Fusion User Group Number of Calling Party |
| 010 | User Group – Ones | Fusion User Group Number of Calling Party |
| 011~026 | Calling Party Number | Calling Party Number (logical ; 16 digits) or Logical Route Number (3 digits) |
| 001 | 0 | Kind of Data : 06 Call Start / End Time |
| 002 | 6 | Kind of Data : 06 Call Start / End Time |
| 003 | 3 | Length of Data : 34 characters |
| 004 | 4 | Length of Data : 34 characters |
| 005 | Year – Thousandths | Call Start : Year |
| 006 | Year – Hundredths | Call Start : Year |
| 007 | Year – Tenths | Call Start : Year |
| 008 | Year – Ones | Call Start : Year |
| 009 | Month – Tenths | Call Start : Month |
| 010 | Month – Ones | Call Start : Month |
| 011 | Day – Tenths | Call Start : Day |
| 012 | Day – Ones | Call Start : Day |
| 013 | Hour – Tenths | Call Start : Hour |
| 014 | Hour – Ones | Call Start : Hour |
| 015 | Minute – Tenths | Call Start : Minute |
| 016 | Minute – Ones | Call Start : Minute |
| 017 | Second – Tenths | Call Start : Second |
| 018 | Second – Ones | Call Start : Second |
| 019 | Millisecond – Hundredths | Call Start : Millisecond |
| 020 | Millisecond – Tenths | Call Start : Millisecond |
| 021 | Millisecond – Ones | Call Start : Millisecond |
| 022 | Year – Thousandths | Call End : Year |
| 023 | Year – Hundredths | Call End : Year |
| 024 | Year – Tenths | Call End : Year |
| 025 | Year – Ones | Call End : Year |
| 026 | Month – Tenths | Call End : Month |
| 027 | Month – Ones | Call End : Month |
| 028 | Day – Tenths | Call End : Day |
| 029 | Day – Ones | Call End : Day |
| 030 | Hour – Tenths | Call End : Hour |
| 031 | Hour – Ones | Call End : Hour |
| 032 | Minute – Tenths | Call End : Minute |
| 033 | Minute – Ones | Call End : Minute |
| 034 | Second – Tenths | Call End : Second |
| 035 | Second – Ones | Call End : Second |
| 036 | Millisecond – Hundredths | Call End : Millisecond |
| 037 | Millisecond – Tenths | Call End : Millisecond |
| 038 | Millisecond – Ones | Call End : Millisecond |
| 001 | 0 | Kind of Data : 07 Account Code |
| 002 | 7 | Kind of Data : 07 Account Code |
| 003 | nan | Length of Data : Variable 1 to 24
01 when no data 16 or 24 maximum
(ASYDL Index 805 can increase the maximum to 24) |
| 004 | nan | Length of Data : Variable 1 to 24
01 when no data 16 or 24 maximum
(ASYDL Index 805 can increase the maximum to 24) |
| 005~020 (005~028) | Account Code | Account Code max 16 or 24 digits
(ASYDL Index 805 can increase the maximum to 24) |
| 001 | 0 | Kind of Data : 08 Condition ‘B’ Codes |
| 002 | 8 | Kind of Data : 08 Condition ‘B’ Codes |
| 003 | 0 | Length of Data : 3 characters |
| 004 | 3 | Length of Data : 3 characters |
| 005 | Condition Code One1 | 0 = No Condition
1 = Call was transferred
2 = Billing is continued
3 = Call was transferred & Billing is continued
4 = Call was transferred to last called party |
| 006 | Condition Code Two1 | Call Origination is:
0 = No Condition
1 = by OG Queuing
2 = by dialing with Account Code
3 = by OG Queuing & dialing with Account Code
4 = by Call Forward Outside
5 = Not Used
6 = by Call Forward Outside & dialing with Account Code |
| 007 | Condition Code Three1 | Call Origination is:
0 = Direct Outgoing
1 = Outgoing via Attendant
2 = Direct Outgoing (Alternate Routing)
3 = Outgoing via Attendant (Alternate Routing)
4 = Direct Outgoing (LCR Routing)
5 = Outgoing via Attendant (LCR Routing)
6 = Direct Outgoing (Called number = first 6 digits of Converted Number)
7 = Outgoing via Attendant (Called number = first 6 digits of Converted Number) |
| 001 | 0 | Kind of Data : 09 Alternate Routing |
| 002 | 9 | Kind of Data : 09 Alternate Routing |
| 003 | 1 | Length of Data : 18 characters |
| 004 | 8 | Length of Data : 18 characters |
| 005 | FPC – Hundredths | Fusion Point Code that was used |
| 006 | FPC – Tenths | Fusion Point Code that was used |
| 007 | FPC – Ones | Fusion Point Code that was used |
| 008 | Route Number – Hundredths | Physical Route Number that was used |
| 009 | Route Number – Tenths | Physical Route Number that was used |
| 010 | Route Number – Ones | Physical Route Number that was used |
| 011 | Route Number – Hundredths | Logical Route Number that was used |
| 012 | Route Number – Tenths | Logical Route Number that was used |
| 013 | Route Number – Ones | Logical Route Number that was used |
| 014 | FPC – Hundredths | Fusion Point Code which was first selected |
| 015 | FPC – Tenths | Fusion Point Code which was first selected |
| 016 | FPC – Ones | Fusion Point Code which was first selected |
| 017 | Route Number – Hundredths | Physical Route Number which was first selected |
| 018 | Route Number – Tenths | Physical Route Number which was first selected |
| 019 | Route Number – Ones | Physical Route Number which was first selected |
| 020 | Route Number – Hundredths | Logical Route Number which was first selected |
| 021 | Route Number – Tenths | Logical Route Number which was first selected |
| 022 | Route Number – Ones | Logical Route Number which was first selected |
| 001 | 1 | Kind of data : 10 Dialed Number |
| 002 | 0 | Kind of data : 10 Dialed Number |
| 003 | nan | Length of Data : Variable 1 to 32
01 when no data 32 maximum |
| 004 | nan | Length of Data : Variable 1 to 32
01 when no data 32 maximum |
| 005~037 | Number Dialed (sent?) | The complete sequence of digits dialed by the caller |
| 001 | 1 | Kind of Data : 11 Office Code Information
(May be omitted) |
| 002 | 1 | Kind of Data : 11 Office Code Information
(May be omitted) |
| 003 | 0 | Length of Data : 8 characters |
| 004 | 8 | Length of Data : 8 characters |
| 005 | Office Code – Thousandths | Office Code of Calling Party |
| 006 | Office Code – Hundredths | Office Code of Calling Party |
| 007 | Office Code – Tenths | Office Code of Calling Party |
| 008 | Office Code – Ones | Office Code of Calling Party |
| 009 | Office Code – Thousandths | Office Code of Billing Process Office |
| 010 | Office Code – Hundredths | Office Code of Billing Process Office |
| 011 | Office Code – Tenths | Office Code of Billing Process Office |
| 012 | Office Code – Ones | Office Code of Billing Process Office |
| 001 | 1 | Kind of Data : 12 Authorization Code |
| 002 | 2 | Kind of Data : 12 Authorization Code |
| 003 | nan | Length of Data : Variable 1 to 16
01 when no data ? 16 maximum |
| 004 | nan | Length of Data : Variable 1 to 16
01 when no data ? 16 maximum |
| 005~020 | Authorization Code | Max 16 digits |
| 001 | 1 | Kind of Data : 13 Call Metering Info + Condition ‘C’ information |
| 002 | 3 | Kind of Data : 13 Call Metering Info + Condition ‘C’ information |
| 003 | nan | Length of Data : Variable 1 to 7
01 when no data 07 maximum |
| 004 | nan | Length of Data : Variable 1 to 7
01 when no data 07 maximum |
| 005 | Charge Information1 | 0 = No Charge Information
1 = 0.1 cent unit
2 = 1 cent unit
3 = 10 cent unit
4 = $1 unit
5 = $10 unit
6 = Calling Metering (4 digits) F = Charge Information Error
If SVI 1588=1 then this bit fixed to ‘1’ |
| 006 | Charge Data (Basic Charge Unit x 100) | Indicates the basic charge unit multiplied by 100 |
| 007 | Charge Data (Basic Charge Unit x 101) | Represents the basic charge unit times 101 |
| 008 | Charge Data (Basic Charge Unit x 102) | Shows the basic charge unit times 102 |
| 009 | Charge Data (Basic Charge Unit x 103) | Denotes the basic charge unit multiplied by 103 |
| 010 | Charge Data (Basic Charge Unit x 104) | Reflects the basic charge unit times 104 |
| 011 | Charge Data (Basic Charge Unit x 105) | Represents the basic charge unit multiplied by 105 |
| 001 | 1 | Kind of Data : 14 Bill Notification Attendant Console + Condition ‘D’ Information |
| 002 | 4 | Kind of Data : 14 Bill Notification Attendant Console + Condition ‘D’ Information |
| 003 | nan | Length of Data : Variable 1 to 4 |
| 004 | nan | Length of Data : Variable 1 to 4 |
| 005 | Bill Notification by Attendant Console | Blank = Not Available
0 = Not Applied
1 = Available |
| 006 | Att Con Number – Hundredth | Attendant Console that is reporting billing |
| 007 | Att Con Number – Tenths | Attendant Console that is reporting billing |
| 008 | Att Con Number – Ones | Attendant Console that is reporting billing |
| 001 | 1 | Kind of Data : 15 Department Code (May be omitted) |
| 002 | 5 | Kind of Data : 15 Department Code (May be omitted) |
| 003 | 0 | Length of Data : 3 characters |
| 004 | 3 | Length of Data : 3 characters |
| 005 | Department Code – Hundredth | Department Code
Also referred to as Group Code. |
| 006 | Department Code – Tenths | Department Code
Also referred to as Group Code. |
| 007 | Department Code – Ones | Department Code
Also referred to as Group Code. |
| 001 | 1 | Kind of Data : 16 Calling Party Number / ANI |
| 002 | 6 | Kind of Data : 16 Calling Party Number / ANI |
| 003 | nan | Length of Data : Variable 1 to 33 |
| 004 | nan | Length of Data : Variable 1 to 34 |
| 005 | ANI Present Identifier | 0 = Unable to output
1 = Display
2 = Unable to Notify
3 = Out of Service (Out of Area)
4 = Public Telephone Origination |
| 006~037 | Calling Party Number | Max 32 digits
ASYDL index 589, bit 6 determines if this is number is displayed as converted by ANEDL/N (EMEA region only) |
| 001 | 1 | Kind of Data : 17 Converted Number
Included when ASYD index 34, bit 5 = 1 |
| 002 | 7 | Kind of Data : 17 Converted Number
Included when ASYD index 34, bit 5 = 1 |
| 003 | nan | Length of Data : Variable 1 to 6 |
| 004 | nan | Length of Data : Variable 1 to 7 |
| 005~010 | Converted Number | First six digits |
| 001 | 1 | Kind of Data : 18 Multi-Area ID (MA-ID)
Included when ASYDL index 589, bit 0 = 1 |
| 002 | 8 | Kind of Data : 18 Multi-Area ID (MA-ID)
Included when ASYDL index 589, bit 0 = 1 |
| 003 | 1 | Length of Data : 10 |
| 004 | 0 | Length of Data : 11 |
| 005 | CP MA-ID – Ten Thousandth | Calling Party’s MA-ID
MA-ID must be between 0001~9999. MA-ID 0000 will not appear in SMDR.
MA-ID must be assigned to a Network, not a Station. |
| 006 | CP MA-ID – Thousandth | Calling Party’s MA-ID
MA-ID must be between 0001~9999. MA-ID 0000 will not appear in SMDR.
MA-ID must be assigned to a Network, not a Station. |
| 007 | CP MA-ID – Hundredth | Calling Party’s MA-ID
MA-ID must be between 0001~9999. MA-ID 0000 will not appear in SMDR.
MA-ID must be assigned to a Network, not a Station. |
| 008 | CP MA-ID – Tenth | Calling Party’s MA-ID
MA-ID must be between 0001~9999. MA-ID 0000 will not appear in SMDR.
MA-ID must be assigned to a Network, not a Station. |
| 009 | CP MA-ID – Ones | Calling Party’s MA-ID
MA-ID must be between 0001~9999. MA-ID 0000 will not appear in SMDR.
MA-ID must be assigned to a Network, not a Station. |
| 010 | Route MA-ID – Ten Thousandth | Seized Route’s MA-ID |
| 011 | Route MA-ID – Thousandth | Seized Route’s MA-ID |
| 012 | Route MA-ID – Hundredth | Seized Route’s MA-ID |
| 013 | Route MA-ID – Tenths | Seized Route’s MA-ID |
| 014 | Route MA-ID – Ones | Seized Route’s MA-ID |
| 001 | ETX | End of Text |
| 01 | Outgoing Trunk / Incoming Trunk information | This field provides information about the trunk that was used for the outgoing or incoming call. |
| 04 | Called Party Information (Physical Number) | This field lists the physical device or line number that received the call. |
| 05† | Called Party Information (Telephone Number) | This optional field contains the actual telephone number of the called party. |
| 06 | Call Start Time / Call End Time | The timestamps marking the initiation and conclusion of the call are provided here. |
| 07† | Account Code | This optional field would contain a code used for billing or accounting purposes related to the call. |
| 08 | Condition B Information | Details regarding specific conditions or call features like transfers or conferencing may be found here. |
| 09 | Alternate Routing Information / Incoming Route Number | This field offers information on any alternative routing the call might have had, including the route number for incoming calls. |
| 10† | Dial Code | An optional field that lists the dial code used, which could denote specific services or destinations. |
| 11† | Office Code Information | This optional field might include a code identifying the office location or department. |
| 12† | Authorization Code | An optional security feature, this code ensures that the caller had the right to make the call. |
| 13† | Condition C Information & Billing Information / Call Metering
Information | An optional field that could include extra call conditions, billing details, and metering information. |
| 16† | Calling Station Number / ANI | The number of the station from where the call was made, or the Automatic Number Identification (ANI) if the call was external. |
| 18† | MA-ID (Multi Area ID) R15 software and above | An optional field applicable for systems with R15 software or higher, indicating a Multi-Area ID that assists in network-wide call management. |

---

## KL RECORD

**Description:** The KL SMDR Record is designed with a flexible format for incoming calls, optimizing data efficiency by compressing the data stream and eliminating redundant gaps. It uses indexes to define the type and length of data, rather than fixed byte sizes.

| CHARACTER | SMDR FIELD NAME AND DESCRIPTION | SMDR FIELD NAME COMMENT |
|---------------------------|----------------------------------|-------------------------|
| 19† | Trunk Call Received Time R20 software and above | Trunk Call Received Time R20 software and above |
| 000 | STX | Start of Text |
| 001 | 0 | System Address; fixed data |
| 002 | ! | Unit Address |
| 003 | Entry Index “K” | “K” = SMDR record |
| 004 | Type of Record “L” | “L” = Incoming Call / Flexible Format |
| 001 | 0 | Kind of Data : 01 Incoming Trunk |
| 002 | 1 | nan |
| 003 | 1 | Length of Data = 12 characters |
| 004 | 2 | nan |
| 005 | FPC – 1 | Fusion Point Code |
| 006 | FPC – 2 | Fusion Point Code |
| 007 | FPC – 3 | Fusion Point Code |
| 008 | Physical Route – Hundredths | Physical Incoming Route Number (ARTD) |
| 009 | Physical Route – Tenths | Physical Incoming Route Number (ARTD) |
| 010 | Physical Route – Ones | Physical Incoming Route Number (ARTD) |
| 011 | Trunk – Hundredths | Trunk Number |
| 012 | Trunk – Tenths | Trunk Number |
| 013 | Trunk – Ones | Trunk Number |
| 014 | Logical Route – Hundredths | Logical Incoming Route (ALRTN) if applicable |
| 015 | Logical Route – Tenths | Logical Incoming Route (ALRTN) if applicable |
| 016 | Logical Route – Ones | Logical Incoming Route (ALRTN) if applicable |
| 001 | 0 | Kind of Data : 04 Called Party Information (Physical number) |
| 002 | 4 | Kind of Data : 04 Called Party Information (Physical number) |
| 003 | 1 | Length of Data = 10 characters |
| 004 | 0 | Length of Data = 10 characters |
| 005 | Called Party Identification | 0 = PBX/CTX (DID) station
1 = Attendant Console
2 = Incoming Trunk |
| 006 | Tenant – 1st digit | Called Party Tenant |
| 007 | Tenant – 2nd digit | Called Party Tenant |
| 008 | Tenant – 3rd digit | Called Party Tenant |
| 009 | Called Number – 1 | Information shown in Called Number fields depends on the Called Party Identification. When character 005 is;
0 – Station number is shown1
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 010 | Called Number – 2 | Information shown in Called Number fields depends on the Called Party Identification. When character 005 is;
0 – Station number is shown1
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 011 | Called Number – 3 | Information shown in Called Number fields depends on the Called Party Identification. When character 005 is;
0 – Station number is shown1
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 012 | Called Number – 4 | Information shown in Called Number fields depends on the Called Party Identification. When character 005 is;
0 – Station number is shown1
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 013 | Called Number – 5 | Information shown in Called Number fields depends on the Called Party Identification. When character 005 is;
0 – Station number is shown1
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 014 | Called Number – 6 | Information shown in Called Number fields depends on the Called Party Identification. When character 005 is;
0 – Station number is shown1
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 001 | 0 | Kind of Data : 05 Called Party Number (Telephone Number or Logical Route) |
| 002 | 5 | Kind of Data : 05 Called Party Number (Telephone Number or Logical Route) |
| 003 | nan | Length of Data : Variable 3 to 22
03 when no data 22 maximum |
| 004 | nan | Length of Data : Variable 3 to 22
03 when no data 22 maximum |
| 005 | Fusion Point Code – 1 | Fusion Point Code of Calling Party : If no Fusion Point Code present then these fields will be set to ‘0’ |
| 006 | Fusion Point Code – 2 | Fusion Point Code of Calling Party : If no Fusion Point Code present then these fields will be set to ‘0’ |
| 007 | Fusion Point Code – 3 | Fusion Point Code of Calling Party : If no Fusion Point Code present then these fields will be set to ‘0’ |
| 008 | User Group – 1 | Fusion User Group Number of Calling Party |
| 009 | User Group – 2 | Fusion User Group Number of Calling Party |
| 010 | User Group – 3 | Fusion User Group Number of Calling Party |
| 011~026 | Called Party Number | Calling Party Number (logical ; 16 digits) or Logical Route Number (3 digits) |
| 001 | 0 | Kind of Data : 06 Call Start / End Time |
| 002 | 6 | Kind of Data : 06 Call Start / End Time |
| 003 | 3 | Length of Data : 34 characters |
| 004 | 4 | Length of Data : 34 characters |
| 005 | Year – Thousandths | Call Start : Year |
| 006 | Year – Hundredths | Call Start : Year |
| 007 | Year – Tenths | Call Start : Year |
| 008 | Year – Ones | Call Start : Year |
| 009 | Month – Tenths | Call Start : Month |
| 010 | Month – Ones | Call Start : Month |
| 011 | Day – Tenths | Call Start : Day |
| 012 | Day – Ones | Call Start : Day |
| 013 | Hour – Tenths | Call Start : Hour |
| 014 | Hour – Ones | Call Start : Hour |
| 015 | Minute – Tenths | Call Start : Minute |
| 016 | Minute – Ones | Call Start : Minute |
| 017 | Second – Tenths | Call Start : Second |
| 018 | Second – Ones | Call Start : Second |
| 019 | Millisecond – Hundredths | Call Start : Millisecond |
| 020 | Millisecond – Tenths | Call Start : Millisecond |
| 021 | Millisecond – Ones | Call Start : Millisecond |
| 022 | Year – Thousandths | Call End : Year |
| 023 | Year – Hundredths | Call End : Year |
| 024 | Year – Tenths | Call End : Year |
| 025 | Year – Ones | Call End : Year |
| 026 | Month – Tenths | Call End : Month |
| 027 | Month – Ones | Call End : Month |
| 028 | Day – Tenths | Call End : Day |
| 029 | Day – Ones | Call End : Day |
| 030 | Hour – Tenths | Call End : Hour |
| 031 | Hour – Ones | Call End : Hour |
| 032 | Minute – Tenths | Call End : Minute |
| 033 | Minute – Ones | Call End : Minute |
| 034 | Second – Tenths | Call End : Second |
| 035 | Second – Ones | Call End : Second |
| 036 | Millisecond – Hundredths | Call End : Millisecond |
| 037 | Millisecond – Tenths | Call End : Millisecond |
| 038 | Millisecond – Ones | Call End : Millisecond |
| 001 | 0 | Kind of Data : 07 Account Code |
| 002 | 7 | Kind of Data : 07 Account Code |
| 003 | nan | Length of Data : Variable 1 to 24
01 when no data 16 or 24 maximum
(ASYDL Index 805 can increase the maximum to 24) |
| 004 | nan | Length of Data : Variable 1 to 24
01 when no data 16 or 24 maximum
(ASYDL Index 805 can increase the maximum to 24) |
| 005~020 | Account Code | Account Code max 16 or 24 digits
(ASYDL Index 805 can increase the maximum to 24) |
| 001 | 0 | Kind of Data : 08 Condition ‘B’ Codes |
| 002 | 8 | Kind of Data : 08 Condition ‘B’ Codes |
| 003 | 0 | Length of Data : 3 characters |
| 004 | 3 | Length of Data : 3 characters |
| 005 | Condition Code One1 | 0 = No Condition
1 = Call was transferred
2 = Billing is continued
3 = Call was transferred & Billing is continued
4 = Call was transferred to last called party |
| 006 | Condition Code Two1 | Call Origination is:
0 = No Condition
1 = by OG Queuing
2 = by dialing with Account Code
3 = by OG Queuing & dialing with Account Code
4 = by Call Forward Outside
5 = Not Used
6 = by Call Forward Outside & dialing with Account Code |
| 007 | Condition Code Three1 | Call Origination is:
0 = Direct Outgoing
1 = Outgoing via Attendant
2 = Direct Outgoing (Alternate Routing)
3 = Outgoing via Attendant (Alternate Routing)
4 = Direct Outgoing (LCR Routing)
5 = Outgoing via Attendant (LCR Routing)
6 = Direct Outgoing (Called number = first 6 digits of Converted Number)
7 = Outgoing via Attendant (Called number = first 6 digits of Converted Number) |
| 001 | 0 | Kind of Data : 09 Alternate Routing |
| 002 | 9 | Kind of Data : 09 Alternate Routing |
| 003 | 1 | Length of Data : 18 characters |
| 004 | 8 | Length of Data : 18 characters |
| 005 | Fusion Point Code – 1st digit | Fusion Point Code that was used |
| 006 | Fusion Point Code – 2nd digit | Fusion Point Code that was used |
| 007 | Fusion Point Code – 3rd digit | Fusion Point Code that was used |
| 008 | Route Number – Hundredths | Physical Route Number that was used |
| 009 | Route Number – Tenths | Physical Route Number that was used |
| 010 | Route Number – Ones | Physical Route Number that was used |
| 011 | Route Number – Hundredths | Logical Route Number that was used |
| 012 | Route Number – Tenths | Logical Route Number that was used |
| 013 | Route Number – Ones | Logical Route Number that was used |
| 014 | Fusion Point Code – 1st digit | Fusion Point Code which was first selected |
| 015 | Fusion Point Code – 2nd digit | Fusion Point Code which was first selected |
| 016 | Fusion Point Code – 3rd digit | Fusion Point Code which was first selected |
| 017 | Route Number – Hundredths | Physical Route Number which was first selected |
| 018 | Route Number – Tenths | Physical Route Number which was first selected |
| 019 | Route Number – Ones | Physical Route Number which was first selected |
| 020 | Route Number – Hundredths | Logical Route Number which was first selected |
| 021 | Route Number – Tenths | Logical Route Number which was first selected |
| 022 | Route Number – Ones | Logical Route Number which was first selected |
| 001 | 1 | Kind of data : 10 Dialed Number |
| 002 | 0 | Kind of data : 10 Dialed Number |
| 003 | nan | Length of Data : Variable 1 to 32
01 when no data 32 maximum |
| 004 | nan | Length of Data : Variable 1 to 32
01 when no data 32 maximum |
| 005~037 | Number Dialed (sent?) | Records the actual number dialed by the caller |
| 001 | 1 | Kind of Data : 11 Office Code Information
(May be omitted) |
| 002 | 1 | nan |
| 003 | 0 | Length of Data : 8 characters |
| 004 | 8 | nan |
| 005 | Office Code – 1st digit | Office Code of Calling Party |
| 006 | Office Code – 2nd digit | Office Code of Calling Party |
| 007 | Office Code – 3rd digit | Office Code of Calling Party |
| 008 | Office Code – 4th digit | Office Code of Calling Party |
| 009 | Office Code – 1st digit | Office Code of Billing Process Office |
| 010 | Office Code – 2nd digit | Stores the dial code used for the call |
| 011 | Office Code – 3rd digit | Captures the office code |
| 012 | Office Code – 4th digit | Records an authorization code |
| 001 | 1 | Kind of Data : 12 Authorization Code |
| 002 | 2 | nan |
| 003 | nan | Length of Data : Variable 1 to 16
01 when no data ? 16 maximum |
| 004 | nan | nan |
| 005~020 | Authorization Code | Max 16 digits |
| 001 | 1 | Kind of Data : 13 Call Metering Info (May be omitted) |
| 002 | 3 | nan |
| 003 | nan | Length of Data : Variable 1 to 7
01 when no data 07 maximum |
| 004 | nan | nan |
| 005 | Charge Information | 0 = No Charge Information
1 = 1 cent unit
2 = 0.1 cent unit
3 = 10 cent unit
4 = $1 unit
5 = $10 unit
6 = Calling Metering (4 digits) F = Charge Information Error
If SVI 1588=1 then this bit fixed to ‘1’

*There is some discrepancy in the definition of byte 005. Some documentation shows the following
difference;
5 = Calling Metering (4 Digit)
6 = Not Used
? = Overbilling |
| 006 | Charge Data (Basic Charge Unit x 100) | Indicates the basic charge unit multiplied by 100 |
| 007 | Charge Data (Basic Charge Unit x 101) | Represents the basic charge unit times 101 |
| 008 | Charge Data (Basic Charge Unit x 102) | Shows the basic charge unit times 102 |
| 009 | Charge Data (Basic Charge Unit x 103) | Denotes the basic charge unit multiplied by 103 |
| 010 | Charge Data (Basic Charge Unit x 104) | Reflects the basic charge unit times 104 |
| 011 | Charge Data (Basic Charge Unit x 105) | Represents the basic charge unit multiplied by 105 |
| 001 | 1 | Kind of Data : 16 Calling Party Number / ANI |
| 002 | 6 | nan |
| 003 | nan | Length of Data : Variable 1 to 33 |
| 004 | nan | nan |
| 005 | Calling Party Number / ANI Present Identifier | 0 = Unable to output
1 = Display
2 = Unable to Notify
3 = Out of Service (Out of Area)
4 = Public Telephone Origination |
| 006~037 | Calling Party Number2 | Max 32 digits*
ASYDL index 589, bit 6 determines if this is number is displayed as converted by ANEDL/N (EMEA region
only)
1. SFI 231/232 might add a leading digit in front of the Calling Party Number in tandem connections.
2. If ACND/N & ACNP/N are used to add digits (such as the Trunk Access Code), they will appear in this
field. |
| 001 | 1 | Kind of Data : 18 Multi-Area ID (MA-ID)
Included when ASYDL index 589, bit 0= 1 |
| 002 | 8 | Kind of Data : 18 Multi-Area ID (MA-ID)
Included when ASYDL index 589, bit 0= 1 |
| 003 | 1 | Length of Data : 10 |
| 004 | 0 | Length of Data : 10 |
| 005 | CP MA-ID – Ten Thousandth | Calling Party’s MA-ID
MA-ID must be between 0001~9999. MA-ID 0000 will not appear in SMDR.
MA-ID must be assigned to a Network, not a Station. |
| 006 | CP MA-ID – Thousandth | Calling Party’s MA-ID
MA-ID must be between 0001~9999. MA-ID 0000 will not appear in SMDR.
MA-ID must be assigned to a Network, not a Station. |
| 007 | CP MA-ID – Hundredth | Calling Party’s MA-ID
MA-ID must be between 0001~9999. MA-ID 0000 will not appear in SMDR.
MA-ID must be assigned to a Network, not a Station. |
| 008 | CP MA-ID – Tenth | Calling Party’s MA-ID
MA-ID must be between 0001~9999. MA-ID 0000 will not appear in SMDR.
MA-ID must be assigned to a Network, not a Station. |
| 009 | CP MA-ID – Ones | Calling Party’s MA-ID
MA-ID must be between 0001~9999. MA-ID 0000 will not appear in SMDR.
MA-ID must be assigned to a Network, not a Station. |
| 010 | Route MA-ID – Ten
Thousand | Seized Route’s MA-ID |
| 011 | Route MA-ID – Thousandth | Seized Route’s MA-ID |
| 012 | Route MA-ID – Hundredth | Seized Route’s MA-ID |
| 013 | Route MA-ID – Tenths | Seized Route’s MA-ID |
| 014 | Route MA-ID – Ones | Seized Route’s MA-ID |
| 001 | 1 | Kind of Data : 19 Trunk Call Received |
| 002 | 9 | Kind of Data : 19 Trunk Call Received |
| 003 | 1 | Length of Data : 34 characters |
| 004 | 7 | Length of Data : 34 characters |
| 005 | Year – Thousandths | Call Start : Year |
| 006 | Year – Hundredths | Call Start : Year |
| 007 | Year – Tenths | Call Start : Year |
| 008 | Year – Ones | Call Start : Year |
| 009 | Month – Tenths | Call Start : Month |
| 010 | Month – Ones | Call Start : Month |
| 011 | Day – Tenths | Call Start : Day |
| 012 | Day – Ones | Call Start : Day |
| 013 | Hour – Tenths | Call Start : Hour |
| 014 | Hour – Ones | Call Start : Hour |
| 015 | Minute – Tenths | Call Start : Minute |
| 016 | Minute – Ones | Call Start : Minute |
| 017 | Second – Tenths | Call Start : Second |
| 018 | Second – Ones | Call Start : Second |
| 019 | Millisecond – Hundredths | Call Start : Millisecond |
| 020 | Millisecond – Tenths | Call Start : Millisecond |
| 021 | Millisecond – Ones | Call Start : Millisecond |
| 001 | ETX | End of Text |

---

## KM RECORD

**Description:** KM Record – Station-to-Station Flexible Format" used in the context of SMDR (Station Message Detail Recording) in telecommunications, specifically for the NEC SV9500 system. This format is designed to efficiently compress the data stream by eliminating unnecessary gaps, contrasting with fixed-byte-size formats

| CHARACTER | SMDR FIELD NAME AND DESCRIPTION | SMDR FIELD NAME COMMENT |
|---------------------------|----------------------------------|-------------------------|
| 02 | Calling Party Information (Physical Number) | [Data for Kind 02] |
| 03† | Calling Party Information (Telephone Number) | [Data for Kind 03] |
| 04 | Called Party Information (Physical Number) | [Data for Kind 04] |
| 05† | Called Party Information (Telephone Number) | [Data for Kind 05] |
| 06 | Call Start Time / Call End Time | [Data for Kind 06] |
| 07† | Account Code | [Data for Kind 07] |
| 08 | Condition B Information | [Data for Kind 08] |
| 18† | MA-ID (Multi Area ID) R15 software and above | [Data for Kind 09] |
| 000 | STX | Start of Text |
| 001 | 0 | System Address; fixed data |
| 002 | ! | Unit Address |
| 003 | Entry Index “K” | “K” = SMDR record |
| 004 | Type of Record “M” | “M” = Station to Station Call / Flexible Format |
| 001 | 0 | Kind of Data : 02 Calling Party Information (Physical number) |
| 002 | 2 | Kind of Data : 02 Calling Party Information (Physical number) |
| 003 | 1 | Length of Data = 10 characters |
| 004 | 0 | Length of Data = 10 characters |
| 005 | Calling Party Identification | 0 = PBX/CTX (DID) station
1 = Attendant Console
2 = Incoming Trunk |
| 006 | Tenant – 1st digit | Calling Party Tenant |
| 007 | Tenant – 2nd digit | Calling Party Tenant |
| 008 | Tenant – 3rd digit | Calling Party Tenant |
| 009 | Calling Number – 1 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 005 is;
0 – Station number is shown
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 010 | Calling Number – 2 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 005 is;
0 – Station number is shown
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 011 | Calling Number – 3 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 005 is;
0 – Station number is shown
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 012 | Calling Number – 4 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 005 is;
0 – Station number is shown
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 013 | Calling Number – 5 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 005 is;
0 – Station number is shown
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 014 | Calling Number – 6 | Information shown in Calling Number fields depends on the Calling Party Identification. When character 005 is;
0 – Station number is shown
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 001 | 0 | Kind of Data : 03 Calling Party Number (Telephone Number) |
| 002 | 3 | Kind of Data : 03 Calling Party Number (Telephone Number) |
| 003 | nan | Length of Data : Variable 3 to 22
03 when no data 22 maximum |
| 004 | nan | Length of Data : Variable 3 to 22
03 when no data 22 maximum |
| 005 | Fusion Point Code – 1 | Fusion Point Code : If no Fusion Point Code present then these fields will be set to ‘0’ |
| 006 | Fusion Point Code – 2 | Fusion Point Code : If no Fusion Point Code present then these fields will be set to ‘0’ |
| 007 | Fusion Point Code – 3 | Fusion Point Code : If no Fusion Point Code present then these fields will be set to ‘0’ |
| 008 | User Group – 1 | Fusion User Group Number |
| 009 | User Group – 2 | Fusion User Group Number |
| 010 | User Group – 3 | Fusion User Group Number |
| 011~026 | Calling Party Number | Calling Party Number (logical ; 16 digits) |
| 001 | 0 | Kind of Data : 04 Called Party Information (Physical number) |
| 002 | 4 | Kind of Data : 04 Called Party Information (Physical number) |
| 003 | 1 | Length of Data = 10 characters |
| 004 | 0 | Length of Data = 10 characters |
| 005 | Called Party Identification | 0 = PBX/CTX (DID) station
1 = Attendant Console
2 = Incoming Trunk |
| 006 | Tenant – 1st digit | Called Party Tenant |
| 007 | Tenant – 2nd digit | Called Party Tenant |
| 008 | Tenant – 3rd digit | Called Party Tenant |
| 009 | Called Number – 1 | Information shown in Called Number fields depends on the Called Party Identification. When character 005 is;
0 – Station number is shown
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 010 | Called Number – 2 | Information shown in Called Number fields depends on the Called Party Identification. When character 005 is;
0 – Station number is shown
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 011 | Called Number – 3 | Information shown in Called Number fields depends on the Called Party Identification. When character 005 is;
0 – Station number is shown
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 012 | Called Number – 4 | Information shown in Called Number fields depends on the Called Party Identification. When character 005 is;
0 – Station number is shown
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 013 | Called Number – 5 | Information shown in Called Number fields depends on the Called Party Identification. When character 005 is;
0 – Station number is shown
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 014 | Called Number – 6 | Information shown in Called Number fields depends on the Called Party Identification. When character 005 is;
0 – Station number is shown
1 – Attendant number is shown
2 – 3 digit Route and Trunk number |
| 001 | 0 | Kind of Data : 05 Called Party Number (Telephone Number) |
| 002 | 5 | Kind of Data : 05 Called Party Number (Telephone Number) |
| 003 | nan | Length of Data : Variable 3 to 22
03 when no data 22 maximum |
| 004 | nan | Length of Data : Variable 3 to 22
03 when no data 22 maximum |
| 005 | Fusion Point Code – 1 | Fusion Point Code : If no Fusion Point Code present then these fields will be set to ‘0’ |
| 006 | Fusion Point Code – 2 | Fusion Point Code : If no Fusion Point Code present then these fields will be set to ‘0’ |
| 007 | Fusion Point Code – 3 | Fusion Point Code : If no Fusion Point Code present then these fields will be set to ‘0’ |
| 008 | User Group – 1 | Fusion User Group Number |
| 009 | User Group – 2 | Fusion User Group Number |
| 010 | User Group – 3 | Fusion User Group Number |
| 011~026 | Calling Party Number | Called Party Number (logical ; 16 digits) |
| 001 | 0 | Kind of Data : 06 Call Start / End Time |
| 002 | 6 | Kind of Data : 06 Call Start / End Time |
| 003 | 3 | Length of Data : 34 characters |
| 004 | 4 | Length of Data : 34 characters |
| 005 | Year – Thousandths | Call Start : Year |
| 006 | Year – Hundredths | Call Start : Year |
| 007 | Year – Tenths | Call Start : Year |
| 008 | Year – Ones | Call Start : Year |
| 009 | Month – Tenths | Call Start : Month |
| 010 | Month – Ones | Call Start : Month |
| 011 | Day – Tenths | Call Start : Day |
| 012 | Day – Ones | Call Start : Day |
| 013 | Hour – Tenths | Call Start : Hour |
| 014 | Hour – Ones | Call Start : Hour |
| 015 | Minute – Tenths | Call Start : Minute |
| 016 | Minute – Ones | Call Start : Minute |
| 017 | Second – Tenths | Call Start : Second |
| 018 | Second – Ones | Call Start : Second |
| 019 | Millisecond – Hundredths | Call Start : Millisecond |
| 020 | Millisecond – Tenths | Call Start : Millisecond |
| 021 | Millisecond – Ones | Call Start : Millisecond |
| 022 | Year – Thousandths | Call End : Year |
| 023 | Year – Hundredths | Call End : Year |
| 024 | Year – Tenths | Call End : Year |
| 025 | Year – Ones | Call End : Year |
| 026 | Month – Tenths | Call End : Month |
| 027 | Month – Ones | Call End : Month |
| 028 | Day – Tenths | Call End : Day |
| 029 | Day – Ones | Call End : Day |
| 030 | Hour – Tenths | Call End : Hour |
| 031 | Hour – Ones | Call End : Hour |
| 032 | Minute – Tenths | Call End : Minute |
| 033 | Minute – Ones | Call End : Minute |
| 034 | Second – Tenths | Call End : Second |
| 035 | Second – Ones | Call End : Second |
| 036 | Millisecond – Hundredths | Call End : Millisecond |
| 037 | Millisecond – Tenths | Call End : Millisecond |
| 038 | Millisecond – Ones | Call End : Millisecond |
| 001 | 0 | Kind of Data : 07 Account Code |
| 002 | 7 | Kind of Data : 07 Account Code |
| 003 | nan | Length of Data : Variable 1 to 24
01 when no data 16 or 24 maximum |
| 004 | nan | Length of Data : Variable 1 to 24
01 when no data 16 or 24 maximum |
| 005~020 | Account Code | Account Code max 16 digits |
| 001 | 0 | Kind of Data : 08 Condition Codes |
| 002 | 8 | Kind of Data : 08 Condition Codes |
| 003 | 0 | Length of Data : 3 characters |
| 004 | 3 | Length of Data : 3 characters |
| 005 | Condition Code Zero (C0)1 | 0 = No Condition
1 = Call was transferred
2 = Billing is continued
3 = Call was transferred & Billing is continued
4 = Call was transferred to last called party |
| 006 | Condition Code One (C1) | Call Origination is:
0 = No Condition
1 = by OG Queuing
2 = by dialing with Account Code
3 = by OG Queuing & dialing with Account Code
4 = by Forward Outside
5 = Not Used
6 = by Forward Outside & dialing with Account Code |
| 007 | Condition Code Two (C2) | Call Origination is:
0 = Direct
1 = via Att Con
2 = Direct (Alternate Routing)
3 = via Att Con (Alternate Routing)
4 = Direct (LCR Routing)
5 = via Att Con (LCR Routing)
6 = Direct (Called number = first 6 digits of Converted Number)
7 = via Att Con (Called number = first 6 digits of Converted Number) |
| 001 | 1 | Kind of data : 10 Dialed Number |
| 002 | 0 | Kind of data : 10 Dialed Number |
| 003 | nan | Length of Data : Variable 1 to 32
01 when no data 32 maximum |
| 004 | nan | Length of Data : Variable 1 to 32
01 when no data 32 maximum |
| 005~037 | Number Dialed (sent?) | Not Used |
| 001 | 1 | Kind of Data : 18 Multi-Area ID (MA-ID)
Included when ASYDL index 589, bit 0= 1 |
| 002 | 8 | Kind of Data : 18 Multi-Area ID (MA-ID)
Included when ASYDL index 589, bit 0= 1 |
| 003 | 1 | Length of Data : 10 |
| 004 | 0 | Length of Data : 10 |
| 005 | CP MA-ID – Ten Thousandth | Calling Party’s MA-ID
MA-ID must be between 0001~9999. MA-ID 0000 will not appear in SMDR.
MA-ID must be assigned to a Network, not a Station. |
| 006 | CP MA-ID – Thousandth | Calling Party’s MA-ID
MA-ID must be between 0001~9999. MA-ID 0000 will not appear in SMDR.
MA-ID must be assigned to a Network, not a Station. |
| 007 | CP MA-ID – Hundredth | Calling Party’s MA-ID
MA-ID must be between 0001~9999. MA-ID 0000 will not appear in SMDR.
MA-ID must be assigned to a Network, not a Station. |
| 008 | CP MA-ID – Tenth | Calling Party’s MA-ID
MA-ID must be between 0001~9999. MA-ID 0000 will not appear in SMDR.
MA-ID must be assigned to a Network, not a Station. |
| 009 | CP MA-ID – Ones | Calling Party’s MA-ID
MA-ID must be between 0001~9999. MA-ID 0000 will not appear in SMDR.
MA-ID must be assigned to a Network, not a Station. |
| 010 | Route MA-ID – Ten
Thousand | Seized Route’s MA-ID |
| 011 | Route MA-ID – Thousandth | Seized Route’s MA-ID |
| 012 | Route MA-ID – Hundredth | Seized Route’s MA-ID |
| 013 | Route MA-ID – Tenths | Seized Route’s MA-ID |
| 014 | Route MA-ID – Ones | Seized Route’s MA-ID |
| 001 | ETX | End of Text |

---

