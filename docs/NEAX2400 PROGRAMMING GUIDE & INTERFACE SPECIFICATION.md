
# SMDR

## NEAX2400

## PROGRAMMING GUIDE

## &

## INTERFACE SPECIFICATIONS

This page is left blank for your notes**<span style="text-decoration:underline;"> </span>**

**SMDR**

Share the information!

Send corrections / omissions to:

<ryoung@necam.com>

Revision History

    1.1 - Changes made to pages 6, 14, 41, and 68.


        2.0 - Reformatted manual to make it easier to read.


        Corrected the KE and KI record breakouts to include the CCIS Office Code.


        Corrected number of called party digits in KA record.


        Added the R14 change to Account Codes for IMX format.


        Added sections covering SMDR over TCP/IP and CCIS breakouts.

**INDEX**

    **<span style="text-decoration:underline;">Section 1 : Programming Information</span>**


    1.0 Programming for Basic SMDR Service 7



    1. Optional Programming for SMDR Service 9
    2. Programming for Serial output of SMDR 12
    3. Programming for TCP/IP output of SMDR (IPX only) 15
    4. Programming for SMDR formats 17

        1.5 Programming considerations for CCIS networks (Centralized SMDR) 19


        1.6 Programming considerations for Fusion networks (Polling Mode) 21


        1.7 Programming considerations for a mixed Fusion/CCIS Network 24


        1.8 Programming considerations for the 2400 IPX UMG 25

###### Section 2 : SMDR Call Record Description

    2.0 KA : Outgoing normal format 27


    2.1 KB : Station to Station normal format 31


    2.2 KE : Incoming normal format 35


    2.3 KH : Outgoing extended format 39


    2.4 KI : Incoming extended format 43


    2.5 KJ : Station to Station extended format 47


    2.6 KK : Outgoing IMX format 51


    2.7 KL : Incoming IMX format 57


    2.8 KM : Station to Station IMX format 63

###### Section 3 : SMDR Over TCP/IP Description

    3.0 Message Sequence 70


    3.1 Ethernet Packet Description 74


    3.2 SMDR Identifiers 78


    **<span style="text-decoration:underline;">Section 4 : CCIS Centralized Billing Message Description</span>**


    4.0 CCIS Message Format: 16-Z 85

###### Section 5 : SMDR Service Conditions and Limitations

    5.0 Service Conditions and Limitations 95


    5.1 SMDR Call Time Specifications 97

###### Section 6 : SMDR Buffer Information for SP & AP

    6.0 SMDR Buffer description 99


    6.1 Buffer Header Information 101

###### Appendix

    A DLSD : Display of Lump SMDR Data 103


    B ATDF : Assignment of Time Difference Data 104


    C How to include both Account Codes and Auth Codes in SMDR 108


    D CPI 3 - OAI Monitored Numbers 109


    E Display Symbol Reference Chart 110


    F Blank SMDR Templates 111

This page is left blank for your notes

**SECTION**

**1**

SMDR PROGRAMMING DESCRIPTION

    This section will explain the programming required for turning on SMDR service as well as explaining the optional programming that is available. The minimum programming requirements on are in **bold** type.

**1.0  <span style="text-decoration:underline;">Programming for Basic SMDR Service</span>**

### Step 1  

    Assign System Data to activate SMDR Service in the PBX.

###

    ASYD: System Data 1


    **Index 32** (_Typically set to 86_)


    Bit 7 : SMDR In Service No/**Yes **0/**1**


    **Index 67** (_Typically set 00 for HP, 80 for MRC_)


    Bit 1 : Send SMDR to Hotel/Motel AP (only flag ‘1’ below 4252 software) **No**/Yes **0**/1


    **ASYD : System Data 2**


    **Index 3 **


    Bit 0 : SMDR output per Tenant No/**Yes **0/**1**


    Bit 7 : SMDR output for internal Station to Station calls No/Yes 0/1

**Step 2 :**

    Assign SMDR Service for the appropriate Service Feature Classes (e.g. this turns SMDR Service on for a particular group of Stations).


    **ASFC**


    SFI 14 : SMDR for trunk calls No/**Yes **0/**1**


    SFI 58 : SMDR for internal Station to Station calls No/Yes 0/1

**Step 3 :**

    Assign SMDR Service to the appropriate routes

#### ARTD : CDN’s that effect SMDR in the outgoing or incoming routes

    CDN 10 : SMDR In Service No/**Yes **0/**1**


    CDN 16 : SMDR2 Detailed Billing Information (this interacts with the ‘toll’ bit in AMND)


    **= 0 **: Outgoing (AMND ‘toll’=0 or 1) calls only


    **= 1** : Outgoing (AMND ‘toll’=0 or 1) and Incoming calls


    **= 2 **: Outgoing (AMND ‘toll’=1) calls only


    **= 3** : Outgoing (AMND ‘toll’=1) and Incoming calls


    CDN 28 : Is Answer Supervision In Service No/Yes 0/1


        _Note – If this CDN is set to ‘1’, then the SMDR record will begin when Answer Supervision has taken place.  If this CDN is set to ‘0’, then ASYD System Data 1, Index 156 (for non-senderized trunks) or Index 157 (for senderized trunks) will be followed._


    **ARTD Cont.**


    CDN 56 : (SMDR3) for Tandem Outgoing calls, create SMDR record Yes/No 0/1


    CDN 69 : (SMDR4) for Tandem Incoming calls, create SMDR record Yes/No 0/1

 **Example of SMDR3 & SMDR4**

    In PBX-B when SMDR3 and SMDR4 are set to ‘0’ for route 1 then:


    - When station-B calls station-A, PBX-C will create an outgoing SMDR record for route 2. PBX-B will create an outgoing SMDR record for route 1 and an incoming SMDR record for route 2.


    In PBX-B when SMDR3 is set to ‘1’ for route 1 and SMDR4 is set to ‘1’ for route 2 then:


    - When station-B calls station-A, PBX-C will create an outgoing SMDR record for route 2.  PBX-B will not create a SMDR record for either route 1 or route 2.

**Step 4 :**

    If only Toll calls are to be recorded, then assign the "Toll" bit for the number pattern to be recorded.

#### AMND

    TOLL : Effective when ARTD CDN-10 is set to ‘1’ and CDN-16 is set to ‘2’ or ‘3’

**1.1  <span style="text-decoration:underline;">Optional Programming for SMDR Service</span>**

# ASYD: System Data 1

    **Index 19**


    Bit 6 : Output format for multiple SMDR ports (A~D) Same information/Split information 0/1


        _Note: This bit is for 5200 MMG/UMG and above.  This will split the SMDR records between two ports such that one record will go out one port (0~3) and the next record will go out the second port (4~7).  The first port must be assigned between ports 0~3 and the second must be 4~7.  In this configuration if one of the two ports goes offline, the other port will also go offline._


    **Index 20**


        Bit 7 : Who is billed in the case of Station-A transferring a call to Station-B who is Call Forwarded-Outside [C-28, C-60, C-74]  Station-A billed/Station-B billed  0/1


         _Note: Two call records will be generated, this bit effects the first._


    **Index 32 **(_Typically set to 86_)


    Bit 0 : Hotel/Motel Feature-When SMDR fails outgoing calls are: Allowed/Restricted 0/1


    Bit 1 : Tenant number for station and route will appear in SMDR record No/Yes 0/1


    Bit 2 : What appears in SMDR Fields 59~61 ARNP Code/Route Number  0/1


    Bit 5 : Include ‘dialed’ access code in SMDR Called Party field No/Yes 0/1


    Bit 6 : Include digits dialed or digits sent in SMDR except access code Sent/Dialed 0/1


        _Note: This bit will effect the entire PBX.  Also see ARTD CDN121._


    **Index 33**


    Bit’s 3 thru 6 work together to provide “total billing” when transfer’s are involved in either an incoming or outgoing call.  “Total Billing” means that a single SMDR record is created instead of a record being created for each transfer.

<table>
  <tr>
   <td><strong>Bit 3</strong>
   </td>
   <td><strong>Bit 4</strong>
   </td>
   <td><em>Only effective when Bit 6=1</em>
   </td>
  </tr>
  <tr>
   <td>0
   </td>
   <td>0
   </td>
   <td>‘Sta. A’ calls ‘Sta. B’ transfers outside ; ‘Sta. A’ Billed
   </td>
  </tr>
  <tr>
   <td>1
   </td>
   <td>0
   </td>
   <td>‘Sta. A’ calls ‘Sta. B’ transfers outside ; ‘Sta. B’ Billed
   </td>
  </tr>
  <tr>
   <td>0
   </td>
   <td>1
   </td>
   <td>‘Sta. A’ calls ‘Sta. B’ transfers to AttCon transfers Outside ; ‘Sta. A’ Billed
   </td>
  </tr>
  <tr>
   <td>1
   </td>
   <td>1
   </td>
   <td>‘Sta. A’ calls ‘Sta. B’ transfers to AttCon transfers Outside ; ‘Sta. B’ Billed
   </td>
  </tr>
</table>

    Bit 5 : Total Billing for Incoming calls (_Last station called is in SMDR_) No/Yes 0/1


    Bit 6 : Total Billing for Outgoing calls (_See bit’s 3 & 4_) No/Yes 0/1


        _Note:  When Bit 5 and/or Bit 6 are set to ‘0’ then there will be a separate SMDR record created each time the call is transferred.  _


    **Index 34**


    Bit 5 : The first six dialed digits are repeated within the SMDR record No/Yes 0/1


    **Index 40**


    Bit 5 : SMDR Buffer Overflow Alarm (6-O and 6-P system messages) 


     (Send 6-O Error Msg @ 80% & Send 6-P Clear Msg @ 50%)**/**(Use Index 249 & 250)  0/1


    **Index 67 **(_Typically set 00 for HP, 80 for MRC_)


    Bit 2 : Hotel/Motel Feature-Restrict outgoing calls on AP failure? No/Yes 0/1


    Bit 3 : Hotel/Motel Feature-Restrict outgoing calls on HP failure? No/Yes 0/1


    Bit 6 : Hotel/Motel Feature-SMDR Control Designation MRC/SMDC 0/1


    Bit 7 : Hotel/Motel Feature-SMDR Sending Designation HP/MRC 0/1


    **ASYD : System Data 1 Cont.**


        **Index 95** : SMDR Memory Clear Timer – If active, this timer will be in effect when the PBX is unable to output SMDR records.  The SMDR buffer will be cleared when this timer expires.  This index is set differently for RDS/HDS and ICS/IMX/IPX.


    <span style="text-decoration:underline;">RDS/HDS</span> _Typically set to 80_


    Timer setting from 82seconds to 2hours 53minutes 57seconds set in 82second increments.


    Bit’s 0~6 : Timer value from 01~7F (TC). TC x 82 = Timer.   Setting 00 defaults to 3hours.


    Bit 7 : Enable SMDR memory clear Yes/No 0/1


    <span style="text-decoration:underline;">ICS/IMX/IPX</span> _Typically set to FF_


    Timer setting from 10minutes to 990minutes in 10minute increments (MTC x TC = Timer).  Setting 00 defaults to 3hours, setting FF disables timer.


    Bit’s 0~3 : MTC – value set from 0~B 


    Bit’s 4~7 : TC – value set from 0~9


    **Index 156** : Trunk Soft Hold Timer ‘A’ (_normally set to 31_)


    On a Non-Senderized Trunk, this timer will start after all of the digits are sent.  If ARTD CDN 28 (ANS) is set to ‘0’, then SMDR billing will begin when this timer expires.  The default for this timer is 18 seconds when the index is set to ‘00’.


    (Timer Value = MTC x TC)


    Bit’s 0~3 : MTC assign from 0~15(F)


    Bit’s 4~7 : TC assign as ‘2’ for 2 seconds.  No other setting valid.


    **Index 157** : Trunk Soft Hold Timer ‘B’ (_normally set to 31_)


    On a Senderized Trunk, this timer will start after all of the digits are sent.  If ARTD CDN 28 (ANS) is set to ‘0’, then SMDR billing will begin when this timer expires.  The default for this timer is 18 seconds when the index is set to ‘00’.


    (Timer Value = MTC x TC)


    Bit’s 0~3 : MTC assign from 0~15(F)


    Bit’s 4~7 : TC assign as ‘2’ for 2 seconds.  No other setting valid.


    **Index 174 **


    Bit 5 : SMDR for CCIS Tandem Office shows Extension Number/Route & Trunk 0/1


    **Index 186**


    Bit 3 : Number of AP’s mounted (RDS/HDS MMG/UMG) Single/Dual 0/1


        _Note: AP’s only function is controlling SMDR.  If an AP is mounted then it will take over SMDR functions from the SP.  If two AP’s are mounted then AP0 will control SMDR for MG’s 0~15 and AP1 will control SMDR for MG’s 16~31.  If one AP fails then the other will take over SMDR for the whole PBX._


    Bit 7 : Include CCIS Office Code (ARNP Rt. 0) with centralized SMDR No/Yes 0/1


        _Note 1: If there is NO office code assigned in ARNP and this index is set to YES, SMDR will stop outputting._


        _Note 2: This must be assigned in ALL nodes in the CCIS network._


    **Index 229**


    Bit 1 : SMDR Department Code output by Authorization Code field No/Yes 0/1


    **Index 240**


    Bit 5 : SMDR outgoing record will show sub-line or prime-line on


        CCIS tandem to outgoing trunk connection Sub-Line/Prime-Line 0/1


    **ASYD : System Data 1 Cont.**


    **Index 241**

Bit 4 : Include incoming ANI from MF/ISDN trunks in SMDR. _SVI 1645_ No/Yes 0/1

_Note 1: only applies to Normal Format, this will overwrite the CCIS Office Code if present.  Do NOT assign this bit when using Extended or IMX format._

_Note 2: ANI will only be present in a KE record generated by a PRI route.  If the PRI tandems across CCIS, the KE for the CCIS will NOT have the ANI._

    **Index 249 **(_Valid when Index 40, bit 5 = 1 ; use with Index 250_)


            Bit’s 0~7 : Determines when an SMDR Buffer Overflow alarm (6-O) will output.  Assign this Index from 05 to 99, where a value of 99hex means the buffer is 99% full.  This Index must be set higher than Index 250.


    **Index 250** (_Valid when Index 40, bit 5 = 1 ; use with Index 249_)


            Bit’s 0~7 : Determines when an SMDR Buffer Overflow clear (6-P) will output.  Assign this Index from 05 to 99, where a value of 99hex means the buffer is 99% full.  This Index must be set lower than Index 249.


    **Index 300**


    Bit 0 : (ICS & up) Expanded SMDR for Centralized Billing-CCIS No/Yes 0/1


    **Index 370**


        Bit 2 : (ICS & up) Allow SMDR to show a Non-CCIS trunk as the originating Route & Trunk in a tandem CCIS call.  _Valid if Index 174, bit 5 = 0 ; SVI 1720_ No/Yes 0/1


    **Index 435**


    Bit 6 : (ICS & up) Length of Authorization Code in SMDR 8 Digits/10 Digits 0/1


        _Note: only effects “Normal Format”. “ICS Extended Format” is fixed to 8 digits.   “IMX Format” allows 10 digits by default._


    **ASYD : System Data 2**


    **Index 3 **


    Bit 6 : For calls across an EPN network show the 🡪 Called & Calling / Called only 0/1


    **ASYDL**


    **Index 641 **


    Bit 0 : SMDR will show the 🡪  Physical Number (ASDT)/Telephone Number (ALGSN) 0/1

##### Note 1 & 2

    Bit 3 : SMDR will show the 🡪 Physical Route (ARTD)/Logical Route (ALRTN) 0/1


        _Note 1 & 2_


        _Note 1: Only available with ICS Extended Format._


            _Note 2: If flagged to show Telephone Number or Logical Route but no Telephone Number or Logical Route exists, then the Physical Number or Route will be displayed._


    **Index 805**


    Bit 5 : Number of digits in Account Code 10 digits/24 digits 0/1


        _Note: Only available in IMX format.  R14 software or higher._

#### ARTD

    CDN 121 (CONV) : SMDR Called Party Number will show 🡪  Number dialed/Number Sent 0/1


        _Note 1: In ICS and below this is found in the ARTE Command._


        _Note 2: When set to Number Dialed, this does not include the Access Code_

**1.2  <span style="text-decoration:underline;">Programming for Serial output of SMDR</span>**

    SMDR will output on the PBX’s I/O card (_Note: This will be the same card/cards that you connect a MAT too.  See Circuit Card Manual to set switch settings for 9600N81_);

* PA-IO02 : RDS/HDS
* PA-IO19 : V70 ICS
* PH-IO24 : ICS/IMX/IPX-T
* PX-IO00 : IPX-I

    A total of four SMDR devices, ‘A’ ~ ‘D’, can be connect to the PBX.  If more than one SMDR port is to be used, all must be connected Serial and use a separate I/O port.  Mixing Serial and TCP/IP connections is not supported.

    If the distance between the I/O card and the SMDR computer exceeds 50 feet (15m), an asynchronous-type modem should be used.

    TIP:  You can test the port and cables by changing it from SMDR to MAT.

**<span style="text-decoration:underline;">RDS/HDS Systems</span>**

# ASYD: System Data 1

    **Index 33**


    Bit 2 : SMDR Output Device (**Business I/O Card** or Hotel CS20)/(SMDC or Hotel CS24) **0**/1


    **Index 34 **(_Set to 09_) : This effects all serial connections, SMDR, MW lamps, etc.


    Bit 0 : SMDR & MCI RS232C output No/**Yes **0/**1**


    Bit 1 : With bit 2 is Parity No Parity **0**/1


    Bit 2 : With bit 1 is Parity No Parity **0**/1


    Bit 3 : With bit 4 is Stop Bits One Stop Bit 0/**1**


    Bit 4 : With bit 3 is Stop Bits One Stop Bit **0**/1


    **Index 35** : I/O Output port for SMDR (<span style="text-decoration:underline;">RDS, HDS systems only</span> / ICS, IMX, IPX use 288)

<table>
  <tr>
   <td>
   </td>
   <td><strong>Port 0</strong>
   </td>
   <td><strong>Port 1</strong>
   </td>
   <td><strong>Port 2</strong>
   </td>
   <td><strong>Port 3</strong>
   </td>
   <td><strong>Port 4</strong>
   </td>
   <td><strong>Port 5</strong>
   </td>
   <td><strong>Port 6</strong>
   </td>
   <td><strong>Port 7</strong>
   </td>
  </tr>
  <tr>
   <td><strong>Assign as:</strong>
   </td>
   <td>01
   </td>
   <td>02
   </td>
   <td>04
   </td>
   <td>08
   </td>
   <td>10
   </td>
   <td>20
   </td>
   <td>40
   </td>
   <td>80
   </td>
  </tr>
</table>

            **Index’s 116 ~ 123** : (<span style="text-decoration:underline;">RDS, HDS systems only</span>) Each of these index’s will set how an I/O port will be used; 116 for port 0, 117 for port 1, etc.  For the index representing the SMDR port, make the assignment ‘**00**’.

#

<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image1.jpg "image_tooltip")

# Cable Connections for Serial SMDR

# <span style="text-decoration:underline;">ICS/IMX/IPX systems</span>

# ASYD: System Data 1

    **Index 33**


    Bit 2 : SMDR Output Device (**Business I/O Card** or Hotel CS20)/(SMDC or Hotel CS24) **0**/1


    **Index 34 **(_Set to 09_) : This effects all serial connections, SMDR, MW lamps, etc.


    Bit 0 : SMDR & MCI RS232C output No/**Yes **0/**1**


    Bit 1 : With bit 2 is Parity No Parity **0**/1


    Bit 2 : With bit 1 is Parity No Parity **0**/1


    Bit 3 : With bit 4 is Stop Bits One Stop Bit 0/**1**


    Bit 4 : With bit 3 is Stop Bits One Stop Bit **0**/1


    **Index 35** : Assign as ‘**00**’.


        **Index 288** : I/O Output port for SMDR “A” (<span style="text-decoration:underline;">ICS, IMX, IPX systems only</span> / For RDS, HDS use Index 35 / **must assign on same port as AIOC**); For expanded SMDR you must also assign Index 296 bit 0 ; assign as follows –

<table>
  <tr>
   <td><em>AIOC Port</em>🡪
   </td>
   <td><strong>Port 0</strong>
   </td>
   <td><strong>Port 1</strong>
   </td>
   <td><strong>Port 2</strong>
   </td>
   <td><strong>Port 3</strong>
   </td>
   <td><strong>Port 4</strong>
   </td>
   <td><strong>Port 5</strong>
   </td>
   <td><strong>Port 6</strong>
   </td>
   <td><strong>Port 7</strong>
   </td>
  </tr>
  <tr>
   <td>
<h3>Expanded</h3>

   </td>
   <td>21
   </td>
   <td>22
   </td>
   <td>24
   </td>
   <td>28
   </td>
   <td>31
   </td>
   <td>32
   </td>
   <td>34
   </td>
   <td>38
   </td>
  </tr>
  <tr>
   <td><strong>Not Expanded</strong>
   </td>
   <td>01
   </td>
   <td>02
   </td>
   <td>04
   </td>
   <td>08
   </td>
   <td>11
   </td>
   <td>12
   </td>
   <td>14
   </td>
   <td>18
   </td>
  </tr>
</table>

        **Index 290** : I/O Output port for SMDR “B” (<span style="text-decoration:underline;">ICS, IMX, IPX systems only</span> / For RDS, HDS use Index 35 / **must assign on same port as AIOC**); For expanded SMDR you must also assign Index 296 bit 0 ; assign as follows –

<table>
  <tr>
   <td><em>AIOC Port</em>🡪
   </td>
   <td><strong>Port 0</strong>
   </td>
   <td><strong>Port 1</strong>
   </td>
   <td><strong>Port 2</strong>
   </td>
   <td><strong>Port 3</strong>
   </td>
   <td><strong>Port 4</strong>
   </td>
   <td><strong>Port 5</strong>
   </td>
   <td><strong>Port 6</strong>
   </td>
   <td><strong>Port 7</strong>
   </td>
  </tr>
  <tr>
   <td>
<h3>Expanded</h3>

   </td>
   <td>21
   </td>
   <td>22
   </td>
   <td>24
   </td>
   <td>28
   </td>
   <td>31
   </td>
   <td>32
   </td>
   <td>34
   </td>
   <td>38
   </td>
  </tr>
  <tr>
   <td><strong>Not Expanded</strong>
   </td>
   <td>01
   </td>
   <td>02
   </td>
   <td>04
   </td>
   <td>08
   </td>
   <td>11
   </td>
   <td>12
   </td>
   <td>14
   </td>
   <td>18
   </td>
  </tr>
</table>

        **Index 292** : I/O Output port for SMDR “C” (<span style="text-decoration:underline;">ICS, IMX, IPX systems only</span> / For RDS, HDS use Index 35 / **must assign on same port as AIOC**); For expanded SMDR you must also assign Index 296 bit 0 ; assign as follows –

<table>
  <tr>
   <td><em>AIOC Port</em>🡪
   </td>
   <td><strong>Port 0</strong>
   </td>
   <td><strong>Port 1</strong>
   </td>
   <td><strong>Port 2</strong>
   </td>
   <td><strong>Port 3</strong>
   </td>
   <td><strong>Port 4</strong>
   </td>
   <td><strong>Port 5</strong>
   </td>
   <td><strong>Port 6</strong>
   </td>
   <td><strong>Port 7</strong>
   </td>
  </tr>
  <tr>
   <td>
<h3>Expanded</h3>

   </td>
   <td>21
   </td>
   <td>22
   </td>
   <td>24
   </td>
   <td>28
   </td>
   <td>31
   </td>
   <td>32
   </td>
   <td>34
   </td>
   <td>38
   </td>
  </tr>
  <tr>
   <td><strong>Not Expanded</strong>
   </td>
   <td>01
   </td>
   <td>02
   </td>
   <td>04
   </td>
   <td>08
   </td>
   <td>11
   </td>
   <td>12
   </td>
   <td>14
   </td>
   <td>18
   </td>
  </tr>
</table>

        **Index 294** : I/O Output port for SMDR “D” (<span style="text-decoration:underline;">ICS, IMX, IPX systems only</span> / For RDS, HDS use Index 35 / **must assign on same port as AIOC**); For expanded SMDR you must also assign Index 296 bit 0 ; assign as follows –

<table>
  <tr>
   <td><em>AIOC Port</em>🡪
   </td>
   <td><strong>Port 0</strong>
   </td>
   <td><strong>Port 1</strong>
   </td>
   <td><strong>Port 2</strong>
   </td>
   <td><strong>Port 3</strong>
   </td>
   <td><strong>Port 4</strong>
   </td>
   <td><strong>Port 5</strong>
   </td>
   <td><strong>Port 6</strong>
   </td>
   <td><strong>Port 7</strong>
   </td>
  </tr>
  <tr>
   <td>
<h3>Expanded</h3>

   </td>
   <td>21
   </td>
   <td>22
   </td>
   <td>24
   </td>
   <td>28
   </td>
   <td>31
   </td>
   <td>32
   </td>
   <td>34
   </td>
   <td>38
   </td>
  </tr>
  <tr>
   <td><strong>Not Expanded</strong>
   </td>
   <td>01
   </td>
   <td>02
   </td>
   <td>04
   </td>
   <td>08
   </td>
   <td>11
   </td>
   <td>12
   </td>
   <td>14
   </td>
   <td>18
   </td>
  </tr>
</table>

    **Index’s 289, 291, 293, and 295** : SMDR Port Failure Alarm Timer


    If a SMDR Serial Port assigned for SMDR “A”, “B”, “C”, or “D” respectively fails, an alarm message can be sent to the system printer.  These Index’s set the timer in minutes that determines when the alarm well be sent.  Values are from 01 to 99.  Setting 00 turns the alarm off.


    **ASYDL**


    **Index 576**


    Bit 2 : SMDR Interface Type **RS232**/LANI  **0**/1

# <span style="text-decoration:underline;">Serial Output of SMDR for ICS/IMX/IPX systems Cont.</span>

#### AIOC

    IOC : Port Number (0~7 : _Must match port assigned in ASYD Index 288~294_)


    Terminal : **4** (SMDR Free Wheeling)


    Protocol : **0** (Free Wheeling)


    Speed : **6** (9600)


    Parity Bit : **0** (No Parity)


    Stop Bit : **1 **(1 Stop Bit)


    Character Bit : **0** (8 Character Bits)

**1.3  <span style="text-decoration:underline;">Programming for TCP/IP output of SMDR</span>**

    SMDR will output on the PC19 in Slot 1 of the IPX-T or the LAN connector of the IPX-I.  Only “IMX Format” is supported with TCP/IP connections.  On the IPX-UMG use the LAN connector on the SP Processor.


    For the SMDR equipment to collect the records over the LAN it must;

* Connect to the IP address of the PBX (i.e. ASYDL index’s 515~518)
* Use port 60010

    A total of four SMDR devices, ‘A’ ~ ‘D’, can be connect to the PBX.  If more than one SMDR port is used, all must be connected TCP/IP.  Mixing Serial and TCP/IP connections is not supported.

    _See Section 3 for more information._

# ASYD: System Data 1

    **Index 288** : set to **00**


    **Index 290** : set to **00**


    **Index 292** : set to **00**


    **Index 294** : set to **00**

#### ASYDL

    **Index 513** : set to **01**


    **Index 515~518** : Assign IP address for the PBX (**must do**)


    **Index 519~522** : Assign Subnet address for the PBX (**must do**)


    **Index 523~526** : Assign Gateway address (if applicable)


    **Index 529**


    Bit 0 : Used with bit 1 for parity No Parity **0**/1


    Bit 1 : Used with bit 0 for parity No Parity **0**/1


    **Index 576**


    Bit 2 : SMDR Interface Type RS-232/**LANI** 0/**1**


    **Index 578**


    Bit 4 : SMDR ‘A’ LAN interface in service No/**Yes **0/**1**


    **Index 579**


    Bit 4 : SMDR ‘B’ LAN interface in service No/Yes 0/1


    **Index 580**


    Bit 4 : SMDR ‘C’ LAN interface in service No/Yes 0/1


    **Index 581**


    Bit 4 : SMDR ‘D’ LAN interface in service No/Yes 0/1

<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image2.png "image_tooltip")

**TCP/IP Port Usage for the IPX CPRBF**

<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image3.png "image_tooltip")

**TCP/IP Port Usage for the IPX CPRRI**

<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image4.png "image_tooltip")

**Cable connections for direct or via HUB**

**1.4  <span style="text-decoration:underline;">Programming for SMDR Formats</span>**

    When using a Serial connection, there are three possible formats that SMDR can be output in; Normal Format, ICS Extended Format, and IMX Format.  When using a TCP/IP connection, only IMX Format is available.


    A total of four SMDR device’s can be connected; ‘A’ ~ ‘D’.  Each device can be a different format.

###### Normal Format (KA, KB, KE type records)

#### ASYD

    **Index 288** : SMDR ‘A’ port assignment


    Bit 5 : SMDR Format **Normal**/Extended **0/**1


    **Index 290** : SMDR ‘B’ port assignment


    Bit 5 : SMDR Format **Normal**/Extended **0/**1


    **Index 292** : SMDR ‘C’ port assignment


    Bit 5 : SMDR Format **Normal**/Extended **0/**1


    **Index 294** : SMDR ‘D’ port assignment


    Bit 5 : SMDR Format **Normal**/Extended **0/**1


    **Index 296**


    Bit 0 : (ICS & up) Expanded SMDR with ANI (KH/KI/KJ records : use with 288) **No**/Yes **0**/1


    **ASYDL**


    **Index 578 **: SMDR “A” Output


    Bit 0 : Output Format for Serial connections **ICS**/IMX **0**/1


    **Index 579** : SMDR “B” Output


    Bit 0 : Output Format for Serial connections **ICS**/IMX **0**/1


    **Index 580** : SMDR “C” Output


    Bit 0 : Output Format for Serial connections **ICS**/IMX **0**/1


    **Index 581** : SMDR “D” Output


    Bit 0 : Output Format for Serial connections **ICS**/IMX **0**/1

###

    <span style="text-decoration:underline;">Examples of Normal, ICS Extended, and IMX Formats</span>


    KA0200090011001..11150941251115094126..........001004020020912142621000....................0000........40987654..01010..........


    KE0100090011000..11150941241115094125..........001000010000................................00002142621001........0101...........


    KH0200130011001..11151006481115100649..........001004020020912142621000....................0000........40987654..01010..........A0................................Z


    KI0100130011000..11151006471115100648..........001000010000................................0000..................0101...........A12142621001......................Z


    KK0112000020015000021000011001..0303000063420011115101135531200111151011435910803004091800002000000002000010129121426210001210409876543213010


    KL0112000010015000041000011000..05030000634200111151011352732001111510114343208030000918000010000000000000161112142621001

###### ICS Extended Format (KH, KI, KJ type records)

#### ASYD

    **Index 241**


    Bit 4 : Include incoming ANI from MF/ISDN trunks in SMDR. _SVI 1645_ **No**/Yes **0**/1


    _Note: When using Centralized SMDR in a CCIS network, this bit may cause ANI to be in the wrong position and/or cause CCIS Office Codes to appear in the record._


    **Index 288** : SMDR ‘A’ port assignment


    Bit 5 : SMDR Format Normal/**Extended** 0**/1**


    **Index 290** : SMDR ‘B’ port assignment


    Bit 5 : SMDR Format Normal/**Extended** 0**/1**


    **Index 292** : SMDR ‘C’ port assignment


    Bit 5 : SMDR Format Normal/**Extended** 0**/1**


    **Index 294** : SMDR ‘D’ port assignment


    Bit 5 : SMDR Format Normal/**Extended** 0**/1**


    **Index 296**


    Bit 0 : (ICS & up) Expanded SMDR with ANI (KH/KI/KJ records : use with 288) No/**Yes** 0/**1**


    **ASYDL**


    **Index 578 **: SMDR “A” Output


    Bit 0 : Output Format for Serial connections **ICS**/IMX **0**/1


    **Index 579** : SMDR “B” Output


    Bit 0 : Output Format for Serial connections **ICS**/IMX **0**/1


    **Index 580** : SMDR “C” Output


    Bit 0 : Output Format for Serial connections **ICS**/IMX **0**/1


    **Index 581** : SMDR “D” Output


    Bit 0 : Output Format for Serial connections **ICS**/IMX **0**/1

###### IMX Format (KK, KL, KM type records)

#### ASYD

    The settings for Index’s 288, 290, 292, 294, and 296 do not matter for IMX Format.


    **ASYDL**


    **Index 578** : SMDR “A” Output


    Bit 0 : Output Format for Serial connections ICS/**IMX** 0/**1**


    **Index 579** : SMDR “B” Output


    Bit 0 : Output Format for Serial connections ICS/**IMX** 0/**1**


    **Index 580** : SMDR “C” Output


    Bit 0 : Output Format for Serial connections ICS/**IMX** 0/**1**


    **Index 581** : SMDR “D” Output


    Bit 0 : Output Format for Serial connections ICS/**IMX** 0/**1**



    1. **<span style="text-decoration:underline;">Programming considerations for CCIS Networks (Centralized SMDR)</span>**

    In a CCIS network, it is possible for all nodes[^1] within the network to send their SMDR records to one ‘central node’ where the SMDR equipment is located.  


    The SMDR records will be created in the node where the calling/called station or trunk resides.  That node will automatically send it across the CCIS Signal Channel once the record is created.


    In CCIS networks with multiple Signal Channels, the channel used for SMDR will vary by system.  In RDS/HDS PBX’s, the Signal Channel for SMDR will be the one listed in ACSC CIC0.  In ICS and above, SMDR will be transmitted across any active Signal Channel.

<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image5.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image5.png "image_tooltip")

#### ASYD : System Data 1

    **Index 174**


    Bit 5 : SMDR for CCIS Tandem Office shows Extension Number/Route & Trunk  0/1


    **Index’s 180 & 181 **: Assign a unique CCIS Point Code for each Node.


            **Index’s 182 & 183** : Assign the CCIS Point Code of the Central Node.  These index’s work together to provide a point code between 1 and 16367.  **Only assign in the remote nodes**.

<table>
  <tr>
   <td><strong>Index</strong>
   </td>
   <td><strong>Bit</strong>
   </td>
   <td><strong>Decimal</strong>
<p>
<strong>Value</strong>
   </td>
   <td><strong>Examples</strong>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td rowspan="8" >182
   </td>
   <td>0
   </td>
   <td>1
   </td>
   <td rowspan="15" >For a Point Code of 10;
<p>
  182 = 0A
<p>
  183 = 00
<p>
For a Point Code of 1001;
<p>
  182 = E9
<p>
  183 = 03
<p>
For a Point Code of 140;
<p>
  182 = 8C
<p>
  183 = 00
   </td>
  </tr>
  <tr>
   <td>1
   </td>
   <td>2
   </td>
  </tr>
  <tr>
   <td>2
   </td>
   <td>4
   </td>
  </tr>
  <tr>
   <td>3
   </td>
   <td>8
   </td>
  </tr>
  <tr>
   <td>4
   </td>
   <td>16
   </td>
  </tr>
  <tr>
   <td>5
   </td>
   <td>32
   </td>
  </tr>
  <tr>
   <td>6
   </td>
   <td>64
   </td>
  </tr>
  <tr>
   <td>7
   </td>
   <td>128
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td rowspan="8" >183
   </td>
   <td>0
   </td>
   <td>256
   </td>
  </tr>
  <tr>
   <td>1
   </td>
   <td>512
   </td>
  </tr>
  <tr>
   <td>2
   </td>
   <td>1024
   </td>
  </tr>
  <tr>
   <td>3
   </td>
   <td>2048
   </td>
  </tr>
  <tr>
   <td>4
   </td>
   <td>4096
   </td>
  </tr>
  <tr>
   <td>5
   </td>
   <td>8192
   </td>
  </tr>
  <tr>
   <td>6
   </td>
   <td>Not Used
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>7
   </td>
   <td>Not Used
   </td>
   <td>
   </td>
  </tr>
</table>

    **ASYD : System Data 1 Cont.**


            **Index 186**


    Bit 7 : Include CCIS Office Code (ARNP Rt. 0) with centralized SMDR No/Yes 0/1


         _Note 1: If there is NO office code assigned in ARNP and this index is set to YES, SMDR will stop outputting_.


        _ Note 2: This must be assigned in ALL nodes in the CCIS network._


    **Index 240**


    Bit 5 : SMDR outgoing record will show sub-line or prime-line on Sub-line/Prime-line 0/1


     CCIS tandem to outgoing trunk connection. 


     (Set in Originating PBX, not Tandem PBX ; May be reversed in RDS/HDS)


    **Index 300**


    Bit 0 : (ICS & up) Expanded SMDR for Centralized Billing-CCIS No/Yes 0/1


    **Index 370**


        Bit 2 : (ICS & up) Allow SMDR to show a Non-CCIS trunk as the originating Route & Trunk in a tandem CCIS call.  _Valid if Index 174, bit 5 = 0 ; SVI 1720_ No/Yes 0/1


    **Trouble Shooting Tip:**


    If SMDR stops being sent from a remote node across CCIS, but will dump out a Serial Port from that remote node; in the remote node change the point code in ASYD Index 182 to some other location, then immediately change it back.  

**1.6  <span style="text-decoration:underline;">Programming considerations for Fusion Networks</span>**

# In a Fusion network, each Node can send it’s SMDR records to a central node, by Fusion Point Code (FPC), where the SMDR equipment is located.  The Remote Nodes will only send records when the Central “Polling” Node sends a request (polls) for the SMDR to be sent

    The Polling Node does not need to be the Network Control Node (NCN).

# ASYDL

    **Index 512 **: Assign the Fusion Point Code for each Node.


    **Index 513 **: Assign as ‘01’ to turn on Local Data Memory


    **Index 576**


    Bit 0 : Fusion Centralized SMDR In Service (polling method) No/**Yes** 0/**1**


    Bit 1 : Collect Station-to-Station fusion calls for Entire Network/Local Node 0/1


        **Index 577 **: Fusion Centralized SMDR.  In the remote PBX’s, assign the FPC of the Polling Node where the SMDR equipment is located.  Assign ‘00’ in the PBX where the SMDR equipment is located.


    **Index 582** : Number of nodes to be polled at one time, set to 01~08


            _Note1: This is assigned only in the Polling Node, in Remote Nodes assign as ‘00’.  _


            _Note2: This is available in R5 and above.  _


            _Note3: A setting of 08 means that all nodes will be polled, not just 8 nodes._


            _Note4: The Polling Node will poll all nodes in the network one at a time by default. This index can set the Polling Node to poll from 1 to 7 nodes at a time or all nodes at once.  _


            _Note5: Default setting 00 will poll 1 node at a time. This is the same as a setting of 01._


    **ASYDL Cont.**


        **Index 583** : This index is a timer that determines when trunk information from a tandem node is sent to the originating node to complete the SMDR record (see figure below for explanation).  The default time is 8 seconds when this index is set to ‘00’.


        Bit’s 0~2 : Assign timer based on chart below

<table>
  <tr>
   <td><strong>Bit 0</strong>
   </td>
   <td><strong>Bit 1</strong>
   </td>
   <td><strong>Bit 2</strong>
   </td>
   <td><strong>Timer</strong>
   </td>
  </tr>
  <tr>
   <td>0
   </td>
   <td>0
   </td>
   <td>0
   </td>
   <td>8 Seconds
   </td>
  </tr>
  <tr>
   <td>1
   </td>
   <td>0
   </td>
   <td>0
   </td>
   <td>2 Seconds
   </td>
  </tr>
  <tr>
   <td>0
   </td>
   <td>1
   </td>
   <td>0
   </td>
   <td>4 Seconds
   </td>
  </tr>
  <tr>
   <td>1
   </td>
   <td>1
   </td>
   <td>0
   </td>
   <td>6 Seconds
   </td>
  </tr>
  <tr>
   <td>0
   </td>
   <td>0
   </td>
   <td>1
   </td>
   <td>8 Seconds
   </td>
  </tr>
  <tr>
   <td>1
   </td>
   <td>0
   </td>
   <td>1
   </td>
   <td>10 Seconds
   </td>
  </tr>
  <tr>
   <td>0
   </td>
   <td>1
   </td>
   <td>1
   </td>
   <td>12 Seconds
   </td>
  </tr>
  <tr>
   <td>1
   </td>
   <td>1
   </td>
   <td>1
   </td>
   <td>14 Seconds
   </td>
  </tr>
</table>

        Bit 7 : Timer in service? No/Yes 0/1

<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image6.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image6.png "image_tooltip")

        **Index 586 **: Set to 99.  This setting determines when SMDR Polling will stop based on how full the SMDR buffer is.  Thus a setting of 99 means that when the buffer is 99% full Polling will stop.  Default setting of 00 is 50%. 


    <p style="text-align: right">
<strong>ASYDL Cont.</strong></p>

        **Index 608 ~ 639** : Assign in Fusion Polling Node only.  These indexes determine what fusion nodes are to be polled for SMDR.  Each bit within each index represents a fusion point code.  See chart below;

<table>
  <tr>
   <td><strong>Index</strong>
   </td>
   <td><strong>Bit 7</strong>
   </td>
   <td><strong>Bit 6</strong>
   </td>
   <td><strong>Bit 5</strong>
   </td>
   <td><strong>Bit 4</strong>
   </td>
   <td><strong>Bit 3</strong>
   </td>
   <td><strong>Bit 2</strong>
   </td>
   <td><strong>Bit 1</strong>
   </td>
   <td><strong>Bit 0</strong>
   </td>
  </tr>
  <tr>
   <td><strong>608</strong>
   </td>
   <td>7
   </td>
   <td>6
   </td>
   <td>5
   </td>
   <td>4
   </td>
   <td>3
   </td>
   <td>2
   </td>
   <td>1
   </td>
   <td>--
   </td>
  </tr>
  <tr>
   <td><strong>609</strong>
   </td>
   <td>15
   </td>
   <td>14
   </td>
   <td>13
   </td>
   <td>12
   </td>
   <td>11
   </td>
   <td>10
   </td>
   <td>9
   </td>
   <td>8
   </td>
  </tr>
  <tr>
   <td><strong>610</strong>
   </td>
   <td>23
   </td>
   <td>22
   </td>
   <td>21
   </td>
   <td>20
   </td>
   <td>19
   </td>
   <td>18
   </td>
   <td>17
   </td>
   <td>16
   </td>
  </tr>
  <tr>
   <td><strong>611</strong>
   </td>
   <td>31
   </td>
   <td>30
   </td>
   <td>29
   </td>
   <td>28
   </td>
   <td>27
   </td>
   <td>26
   </td>
   <td>25
   </td>
   <td>24
   </td>
  </tr>
  <tr>
   <td><strong>612</strong>
   </td>
   <td>39
   </td>
   <td>38
   </td>
   <td>37
   </td>
   <td>36
   </td>
   <td>35
   </td>
   <td>34
   </td>
   <td>33
   </td>
   <td>32
   </td>
  </tr>
  <tr>
   <td><strong>613</strong>
   </td>
   <td>47
   </td>
   <td>46
   </td>
   <td>45
   </td>
   <td>44
   </td>
   <td>43
   </td>
   <td>42
   </td>
   <td>41
   </td>
   <td>40
   </td>
  </tr>
  <tr>
   <td><strong>614</strong>
   </td>
   <td>55
   </td>
   <td>54
   </td>
   <td>53
   </td>
   <td>52
   </td>
   <td>51
   </td>
   <td>50
   </td>
   <td>49
   </td>
   <td>48
   </td>
  </tr>
  <tr>
   <td><strong>615</strong>
   </td>
   <td>63
   </td>
   <td>62
   </td>
   <td>61
   </td>
   <td>60
   </td>
   <td>59
   </td>
   <td>58
   </td>
   <td>57
   </td>
   <td>56
   </td>
  </tr>
  <tr>
   <td><strong>616</strong>
   </td>
   <td>71
   </td>
   <td>70
   </td>
   <td>69
   </td>
   <td>68
   </td>
   <td>67
   </td>
   <td>66
   </td>
   <td>65
   </td>
   <td>64
   </td>
  </tr>
  <tr>
   <td><strong>617</strong>
   </td>
   <td>79
   </td>
   <td>78
   </td>
   <td>77
   </td>
   <td>76
   </td>
   <td>75
   </td>
   <td>74
   </td>
   <td>73
   </td>
   <td>72
   </td>
  </tr>
  <tr>
   <td><strong>618</strong>
   </td>
   <td>87
   </td>
   <td>86
   </td>
   <td>85
   </td>
   <td>84
   </td>
   <td>83
   </td>
   <td>82
   </td>
   <td>81
   </td>
   <td>80
   </td>
  </tr>
  <tr>
   <td><strong>619</strong>
   </td>
   <td>95
   </td>
   <td>94
   </td>
   <td>93
   </td>
   <td>92
   </td>
   <td>91
   </td>
   <td>90
   </td>
   <td>89
   </td>
   <td>88
   </td>
  </tr>
  <tr>
   <td><strong>620</strong>
   </td>
   <td>103
   </td>
   <td>102
   </td>
   <td>101
   </td>
   <td>100
   </td>
   <td>99
   </td>
   <td>98
   </td>
   <td>97
   </td>
   <td>96
   </td>
  </tr>
  <tr>
   <td><strong>621</strong>
   </td>
   <td>111
   </td>
   <td>110
   </td>
   <td>109
   </td>
   <td>108
   </td>
   <td>107
   </td>
   <td>106
   </td>
   <td>105
   </td>
   <td>104
   </td>
  </tr>
  <tr>
   <td><strong>622</strong>
   </td>
   <td>119
   </td>
   <td>118
   </td>
   <td>117
   </td>
   <td>116
   </td>
   <td>115
   </td>
   <td>114
   </td>
   <td>113
   </td>
   <td>112
   </td>
  </tr>
  <tr>
   <td><strong>623</strong>
   </td>
   <td>127
   </td>
   <td>126
   </td>
   <td>125
   </td>
   <td>124
   </td>
   <td>123
   </td>
   <td>122
   </td>
   <td>121
   </td>
   <td>120
   </td>
  </tr>
  <tr>
   <td><strong>624</strong>
   </td>
   <td>135
   </td>
   <td>134
   </td>
   <td>133
   </td>
   <td>132
   </td>
   <td>131
   </td>
   <td>130
   </td>
   <td>129
   </td>
   <td>128
   </td>
  </tr>
  <tr>
   <td><strong>625</strong>
   </td>
   <td>143
   </td>
   <td>142
   </td>
   <td>141
   </td>
   <td>140
   </td>
   <td>139
   </td>
   <td>138
   </td>
   <td>137
   </td>
   <td>136
   </td>
  </tr>
  <tr>
   <td><strong>626</strong>
   </td>
   <td>151
   </td>
   <td>150
   </td>
   <td>149
   </td>
   <td>148
   </td>
   <td>147
   </td>
   <td>146
   </td>
   <td>145
   </td>
   <td>144
   </td>
  </tr>
  <tr>
   <td><strong>627</strong>
   </td>
   <td>159
   </td>
   <td>158
   </td>
   <td>157
   </td>
   <td>156
   </td>
   <td>155
   </td>
   <td>154
   </td>
   <td>153
   </td>
   <td>152
   </td>
  </tr>
  <tr>
   <td><strong>628</strong>
   </td>
   <td>167
   </td>
   <td>166
   </td>
   <td>165
   </td>
   <td>164
   </td>
   <td>163
   </td>
   <td>162
   </td>
   <td>161
   </td>
   <td>160
   </td>
  </tr>
  <tr>
   <td><strong>629</strong>
   </td>
   <td>175
   </td>
   <td>174
   </td>
   <td>173
   </td>
   <td>172
   </td>
   <td>171
   </td>
   <td>170
   </td>
   <td>169
   </td>
   <td>168
   </td>
  </tr>
  <tr>
   <td><strong>630</strong>
   </td>
   <td>183
   </td>
   <td>182
   </td>
   <td>181
   </td>
   <td>180
   </td>
   <td>179
   </td>
   <td>178
   </td>
   <td>177
   </td>
   <td>176
   </td>
  </tr>
  <tr>
   <td><strong>631</strong>
   </td>
   <td>191
   </td>
   <td>190
   </td>
   <td>189
   </td>
   <td>188
   </td>
   <td>187
   </td>
   <td>186
   </td>
   <td>185
   </td>
   <td>184
   </td>
  </tr>
  <tr>
   <td><strong>632</strong>
   </td>
   <td>199
   </td>
   <td>198
   </td>
   <td>197
   </td>
   <td>196
   </td>
   <td>195
   </td>
   <td>194
   </td>
   <td>193
   </td>
   <td>192
   </td>
  </tr>
  <tr>
   <td><strong>633</strong>
   </td>
   <td>207
   </td>
   <td>206
   </td>
   <td>205
   </td>
   <td>204
   </td>
   <td>203
   </td>
   <td>202
   </td>
   <td>201
   </td>
   <td>200
   </td>
  </tr>
  <tr>
   <td><strong>634</strong>
   </td>
   <td>215
   </td>
   <td>214
   </td>
   <td>213
   </td>
   <td>212
   </td>
   <td>211
   </td>
   <td>210
   </td>
   <td>209
   </td>
   <td>208
   </td>
  </tr>
  <tr>
   <td><strong>635</strong>
   </td>
   <td>223
   </td>
   <td>222
   </td>
   <td>221
   </td>
   <td>220
   </td>
   <td>219
   </td>
   <td>218
   </td>
   <td>217
   </td>
   <td>216
   </td>
  </tr>
  <tr>
   <td><strong>636</strong>
   </td>
   <td>231
   </td>
   <td>230
   </td>
   <td>229
   </td>
   <td>228
   </td>
   <td>227
   </td>
   <td>226
   </td>
   <td>225
   </td>
   <td>224
   </td>
  </tr>
  <tr>
   <td><strong>637</strong>
   </td>
   <td>239
   </td>
   <td>238
   </td>
   <td>237
   </td>
   <td>236
   </td>
   <td>235
   </td>
   <td>234
   </td>
   <td>233
   </td>
   <td>232
   </td>
  </tr>
  <tr>
   <td><strong>638</strong>
   </td>
   <td>247
   </td>
   <td>246
   </td>
   <td>245
   </td>
   <td>244
   </td>
   <td>243
   </td>
   <td>242
   </td>
   <td>241
   </td>
   <td>240
   </td>
  </tr>
  <tr>
   <td><strong>639</strong>
   </td>
   <td>--
   </td>
   <td>--
   </td>
   <td>253
   </td>
   <td>252
   </td>
   <td>251
   </td>
   <td>250
   </td>
   <td>249
   </td>
   <td>248
   </td>
  </tr>
</table>

**1.7  <span style="text-decoration:underline;">Prgramming considerations for a Mixed Fusion/CCIS Network</span>**

    To collect SMDR at one node in a mixed Fusion/CCIS network, you must first send all of the SMDR from the CCIS network to a node on the fusion network.  That means that the switch that is connected to both the Fusion network and the CCIS network will become the CCIS Centralized SMDR Node.  The CCIS Centralized SMDR Node can be any Node in the Fusion Network, including the Fusion Polling Node.


    **ASYDL**


            **Index 585** : When the CCIS Centralized Node is NOT the Fusion Polling Node, this index can be set in the Fusion Polling Node to change the polling cycle timer.  This would be done to prevent SMDR buffer overflow in the CCIS Centralized Node.  The default setting of ‘00’ is a value of 2 seconds.

<table>
  <tr>
   <td><strong>Polling Cycle</strong>
   </td>
   <td><strong>System Data</strong>
   </td>
   <td rowspan="9" >
   </td>
   <td><strong>Polling Cycle</strong>
   </td>
   <td><strong>System Data</strong>
   </td>
  </tr>
  <tr>
   <td>0.25sec
   </td>
   <td>01
   </td>
   <td>2.25sec
   </td>
   <td>09
   </td>
  </tr>
  <tr>
   <td>0.50sec
   </td>
   <td>02
   </td>
   <td>2.50sec
   </td>
   <td>0A
   </td>
  </tr>
  <tr>
   <td>0.75sec
   </td>
   <td>03
   </td>
   <td>2.75sec
   </td>
   <td>0B
   </td>
  </tr>
  <tr>
   <td>1.00sec
   </td>
   <td>04
   </td>
   <td>3.00sec
   </td>
   <td>0C
   </td>
  </tr>
  <tr>
   <td>1.25sec
   </td>
   <td>05
   </td>
   <td>3.25sec
   </td>
   <td>0D
   </td>
  </tr>
  <tr>
   <td>1.50sec
   </td>
   <td>06
   </td>
   <td>3.50sec
   </td>
   <td>0E
   </td>
  </tr>
  <tr>
   <td>1.75sec
   </td>
   <td>07
   </td>
   <td>3.75sec
   </td>
   <td>0F
   </td>
  </tr>
  <tr>
   <td>2.00sec
   </td>
   <td>08
   </td>
   <td>4.00sec
   </td>
   <td>10
   </td>
  </tr>
</table>

            ** **

**1.8  <span style="text-decoration:underline;">Programming considerations for the 2400 IPX UMG</span>**

    Each Local Processor (LP) in the IPX UMG buffers SMDR for the 8 Module Groups (wall) it controls.  Thus in a full UMG, 32 Module Groups, there will be 4 LP’s buffering SMDR.  The System Processor (SP) will “Poll” each LP to send the SMDR just as the “Polling Node” in a Fusion Network would.  


    In a “stand alone” IPX UMG, fusion point codes are not necessary for SMDR polling to operate.  The SP poll’s the PBI number of the LP’s, not the point code.


        **ASYDL**


        **Index 584** :  Internal polling cycle for IPX UMG only.

<table>
  <tr>
   <td><strong>Polling Cycle</strong>
   </td>
   <td><strong>System Data</strong>
   </td>
   <td rowspan="9" >
   </td>
   <td><strong>Polling Cycle</strong>
   </td>
   <td><strong>System Data</strong>
   </td>
  </tr>
  <tr>
   <td>0.25sec
   </td>
   <td>01
   </td>
   <td>2.25sec
   </td>
   <td>09
   </td>
  </tr>
  <tr>
   <td>0.50sec
   </td>
   <td>02
   </td>
   <td>2.50sec
   </td>
   <td>0A
   </td>
  </tr>
  <tr>
   <td>0.75sec
   </td>
   <td>03
   </td>
   <td>2.75sec
   </td>
   <td>0B
   </td>
  </tr>
  <tr>
   <td>1.00sec
   </td>
   <td>04
   </td>
   <td>3.00sec
   </td>
   <td>0C
   </td>
  </tr>
  <tr>
   <td>1.25sec
   </td>
   <td>05
   </td>
   <td>3.25sec
   </td>
   <td>0D
   </td>
  </tr>
  <tr>
   <td>1.50sec
   </td>
   <td>06
   </td>
   <td>3.50sec
   </td>
   <td>0E
   </td>
  </tr>
  <tr>
   <td>1.75sec
   </td>
   <td>07
   </td>
   <td>3.75sec
   </td>
   <td>0F
   </td>
  </tr>
  <tr>
   <td>2.00sec
   </td>
   <td>08
   </td>
   <td>4.00sec
   </td>
   <td>10
   </td>
  </tr>
</table>

This page is left blank for your notes

**SECTION**

**2**

**SMDR CALL RECORD DESCRIPTION**

**2.0  <span style="text-decoration:underline;">KA Record – Normal Format – Outgoing</span>**

    Programming information for this format can be found in Section 1.4

**Example:**

<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image7.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image7.jpg "image_tooltip")
**<span style="text-decoration:underline;">KA Record Cont:</span>**

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>000
   </td>
   <td>STX
   </td>
   <td>Start of Text
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>SA
   </td>
   <td>System Address; fixed data
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>UA
   </td>
   <td>Unit Address
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>Entry Index “K”
   </td>
   <td>“K” = SMDR record
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>Type of Record “A”
   </td>
   <td>“A” = Outgoing Call / Normal Format
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Route Number – Hundredths
   </td>
   <td rowspan="6" >Outgoing Route and Trunk information
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>Route Number – Tenths
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>Route Number – Ones
   </td>
  </tr>
  <tr>
   <td>008
   </td>
   <td>Trunk Number – Hundredths
   </td>
  </tr>
  <tr>
   <td>009
   </td>
   <td>Trunk Number – Tenths
   </td>
  </tr>
  <tr>
   <td>010
   </td>
   <td>Trunk Number – Ones
   </td>
  </tr>
  <tr>
   <td>011
   </td>
   <td>Calling Party Identification
   </td>
   <td>0 = PBX/CTX (DID) station
<p>
1 = Attendant Console
<p>
2 = Incoming Trunk
<p>
3 = Monitored Number (<em>Note</em>)
   </td>
  </tr>
  <tr>
   <td>012
   </td>
   <td>Tenant – 1<sup>st</sup> digit
   </td>
   <td rowspan="2" >Only in 1000 & 2000 (RDS) Feature Packages.  3000 and above, fields are blank.
   </td>
  </tr>
  <tr>
   <td>013
   </td>
   <td>Tenant – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>014
   </td>
   <td>Calling Number – 1
   </td>
   <td rowspan="6" >Information shown in Calling Number fields depends on the Calling Party Identification.  When character 011 is;
<p>
0 – Station number is shown
<p>
1 – Attendant number is shown
<p>
2 – 3 digit Route and Trunk number
   </td>
  </tr>
  <tr>
   <td>015
   </td>
   <td>Calling Number – 2
   </td>
  </tr>
  <tr>
   <td>016
   </td>
   <td>Calling Number – 3
   </td>
  </tr>
  <tr>
   <td>017
   </td>
   <td>Calling Number – 4
   </td>
  </tr>
  <tr>
   <td>018
   </td>
   <td>Calling Number – 5
   </td>
  </tr>
  <tr>
   <td>019
   </td>
   <td>Calling Number – 6
   </td>
  </tr>
  <tr>
   <td>020
   </td>
   <td>Month – Tenths
   </td>
   <td rowspan="10" >Time when SMDR record begins
<p>
For Station-To-Station this time begins when called party answers.
<p>
For Station-To-Route the SMDR record begins when Answer Supervision has taken place.  This is effected by ARTD CDN28 or ASYD Index 156 & 157.
   </td>
  </tr>
  <tr>
   <td>021
   </td>
   <td>Month – Ones
   </td>
  </tr>
  <tr>
   <td>022
   </td>
   <td>Day – Tenths
   </td>
  </tr>
  <tr>
   <td>023
   </td>
   <td>Day – Ones
   </td>
  </tr>
  <tr>
   <td>024
   </td>
   <td>Hour – Tenths
   </td>
  </tr>
  <tr>
   <td>025
   </td>
   <td>Hour – Ones
   </td>
  </tr>
  <tr>
   <td>026
   </td>
   <td>Minute – Tenths
   </td>
  </tr>
  <tr>
   <td>027
   </td>
   <td>Minute – Ones
   </td>
  </tr>
  <tr>
   <td>028
   </td>
   <td>Second – Tenths
   </td>
  </tr>
  <tr>
   <td>029
   </td>
   <td>Second – Ones
   </td>
  </tr>
  <tr>
   <td>030
   </td>
   <td>Month –Tenths
   </td>
   <td rowspan="10" >Time when SMDR record is complete
   </td>
  </tr>
  <tr>
   <td>031
   </td>
   <td>Month – Ones
   </td>
  </tr>
  <tr>
   <td>032
   </td>
   <td>Day – Tenths
   </td>
  </tr>
  <tr>
   <td>033
   </td>
   <td>Day – Ones
   </td>
  </tr>
  <tr>
   <td>034
   </td>
   <td>Hour – Tenths
   </td>
  </tr>
  <tr>
   <td>035
   </td>
   <td>Hour – Ones
   </td>
  </tr>
  <tr>
   <td>036
   </td>
   <td>Minute – Tenths
   </td>
  </tr>
  <tr>
   <td>037
   </td>
   <td>Minute – Ones
   </td>
  </tr>
  <tr>
   <td>038
   </td>
   <td>Second – Tenths
   </td>
  </tr>
  <tr>
   <td>039
   </td>
   <td>Second – Ones
   </td>
  </tr>
  <tr>
   <td>040~049
   </td>
   <td>Account Code (max 10 digits)
   </td>
   <td>Blank if Account Code not present
   </td>
  </tr>
  <tr>
   <td>050
   </td>
   <td>Tenant – 1<sup>st</sup> digit
   </td>
   <td rowspan="3" >Calling Party Tenant Information
<p>
This is for 3000 Series Feature Package and higher.
   </td>
  </tr>
  <tr>
   <td>051
   </td>
   <td>Tenant – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>052
   </td>
   <td>Tenant – 3<sup>rd</sup> digit
   </td>
  </tr>
</table>

_Note: See Appendix D_**<span style="text-decoration:underline;">KA Record Cont:</span>**

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>053
   </td>
   <td>Condition Code One
   </td>
   <td>0 = Call has not transferred
<p>
1 = Call has been transferred
<p>
Example:
<p>
Station-A calls Station-B, talks for 10 minutes then transfers outside to Station-C.  The SMDR record will show Condition 1.
<p>
(<em>Note: ASYD System 1 Index 33 will effect who is billed on a transfer</em>)
   </td>
  </tr>
  <tr>
   <td>054
   </td>
   <td>Condition Code Two
   </td>
   <td>0 = Incoming, Outgoing, or Tandem call with neither Outgoing Trunk Queuing nor Account Codes used.
<p>
1 = Outgoing Trunk Queuing used, but not Account Codes.
<p>
2 = Account Codes used, but not Outgoing Trunk Queuing.
<p>
3 = Both Outgoing Trunk Queuing and Account Codes used.
   </td>
  </tr>
  <tr>
   <td>055
   </td>
   <td>Condition Code Three
   </td>
   <td>0 = Regular Outgoing or Tandem call.
<p>
1 = Attendant Operator assisted call.
<p>
2 = The call Route Advanced (AOPR).
<p>
3 = Attendant Operator assisted call that Route Advanced.
<p>
4 = Call routed to Least Cost Routing.
<p>
5 = Attendant Operator assisted call that is routed to Least Cost Routing.
   </td>
  </tr>
  <tr>
   <td>056
   </td>
   <td>Selected Route – Hundredths
   </td>
   <td rowspan="3" >When Condition Code Three shows 2 through 5, this shows the selected route.
<p>
Otherwise this field blank.
   </td>
  </tr>
  <tr>
   <td>057
   </td>
   <td>Selected Route – Tenths
   </td>
  </tr>
  <tr>
   <td>058
   </td>
   <td>Selected Route – Ones
   </td>
  </tr>
  <tr>
   <td>059
   </td>
   <td>First Route – Hundredths
   </td>
   <td rowspan="3" >When Condition Code Three shows 2 through 5, this shows the First Choice route.  Otherwise this field blank.
<p>
If ASYD System 1, Index 32, Bit 2 = 0 then ARNP for the selected route will be in this field.  If ARNP is set to * then ‘011’ will be here.  If ARNP is set to # then ‘012’ will be here.
   </td>
  </tr>
  <tr>
   <td>060
   </td>
   <td>First Route – Tenths
   </td>
  </tr>
  <tr>
   <td>061
   </td>
   <td>First Route – Ones
   </td>
  </tr>
</table>

**<span style="text-decoration:underline;">KA Record Cont:</span>**

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name and Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>062~085
   </td>
   <td>Called Number (max 24 digits)
   </td>
   <td>If ASYD System 1, Index 32, Bit 5 = 1 then the dialed access code (i.e. 9) is included.
<p>
When ASYD System 1, Index 32, Bit 6 =
<p>
0 – Digits sent are in this field (after AOPR, AADT, etc.)
<p>
1 – Digits dialed are in this field (except access code)
<p>
When ARTD CDN 121 =
<p>
0 – Digits sent are in this field (after AOPR, AADT, etc.)
<p>
1 – Digits dialed are in this field (except the access code)
<p>
<em>Note: This overrides ASYD above.</em>
   </td>
  </tr>
  <tr>
   <td>086~093
   </td>
   <td>Not Used
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>094
   </td>
   <td>Metering Pulse – Thousands
   </td>
   <td rowspan="4" >When Metering Pulses are received from C.O., they will be in this field.  Default is all ‘0’.
   </td>
  </tr>
  <tr>
   <td>095
   </td>
   <td>Metering Pulse – Hundredths
   </td>
  </tr>
  <tr>
   <td>096
   </td>
   <td>Metering Pulse – Tenths
   </td>
  </tr>
  <tr>
   <td>097
   </td>
   <td>Metering Pulse – Ones
   </td>
  </tr>
  <tr>
   <td>098
   </td>
   <td>Office Code 1 (Digit 1)
   </td>
   <td rowspan="4" >CCIS Office Code from ARNP Route 0 in the Originating PBX.  When ASYD Index 186 Bit 7 = 1
   </td>
  </tr>
  <tr>
   <td>099
   </td>
   <td>Office Code 1 (Digit 2)
   </td>
  </tr>
  <tr>
   <td>100
   </td>
   <td>Office Code 1 (Digit 3)
   </td>
  </tr>
  <tr>
   <td>101
   </td>
   <td>Office Code 1 (Digit 4)
   </td>
  </tr>
  <tr>
   <td>102
   </td>
   <td>Office Code 2 (Digit 1)
   </td>
   <td rowspan="4" >CCIS Office Code from ARNP Route 0 in the Billing PBX (PBX that created the SMDR record).  When ASYD Index 186 Bit 7 = 1
   </td>
  </tr>
  <tr>
   <td>103
   </td>
   <td>Office Code 2 (Digit 2)
   </td>
  </tr>
  <tr>
   <td>104
   </td>
   <td>Office Code 2 (Digit 3)
   </td>
  </tr>
  <tr>
   <td>105
   </td>
   <td>Office Code 2 (Digit 4)
   </td>
  </tr>
  <tr>
   <td>106~115
   </td>
   <td>Authorization Code
   </td>
   <td>Procedure 2 Auth Code Only
<p>
Max digits effected by ASYD Index 435;
<p>
Bit 6 = 0 : Max 8 digits
<p>
Bit 6 = 1 : Max 10 digits
   </td>
  </tr>
  <tr>
   <td>116
   </td>
   <td>Year – Tenths
   </td>
   <td rowspan="2" >Year of start of conversation
   </td>
  </tr>
  <tr>
   <td>117
   </td>
   <td>Year – Ones
   </td>
  </tr>
  <tr>
   <td>118
   </td>
   <td>Year – Tenths
   </td>
   <td rowspan="2" >Year of end of conversation
   </td>
  </tr>
  <tr>
   <td>119
   </td>
   <td>Year – Ones
   </td>
  </tr>
  <tr>
   <td>120
   </td>
   <td>Set to ‘0’
   </td>
   <td>ISDN Billing indication
   </td>
  </tr>
  <tr>
   <td>121~130
   </td>
   <td>Blank
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>131
   </td>
   <td>ETX
   </td>
   <td>End of Text
   </td>
  </tr>
</table>

**2.1  <span style="text-decoration:underline;">KB Record – Normal Format – Station to Station</span>**

    Programming information for this format can be found in Section 1.4

#### Example

    **<span style="text-decoration:underline;">KB Record Cont:</span>**

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>000
   </td>
   <td>STX
   </td>
   <td>Start of Text
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>SA
   </td>
   <td>System Address; fixed data
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>UA
   </td>
   <td>Unit Address
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>Entry Index “K”
   </td>
   <td>“K” = SMDR record
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>Type of Record “B”
   </td>
   <td>“B” = Station to Station / Normal Format
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Blank
   </td>
   <td rowspan="6" >For Station-To-Station calls, 005~010 are blank
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>Blank
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>Blank
   </td>
  </tr>
  <tr>
   <td>008
   </td>
   <td>Blank
   </td>
  </tr>
  <tr>
   <td>009
   </td>
   <td>Blank
   </td>
  </tr>
  <tr>
   <td>010
   </td>
   <td>Blank
   </td>
  </tr>
  <tr>
   <td>011
   </td>
   <td>Calling Party Identification
   </td>
   <td>0 = PBX/CTX (DID) station
<p>
1 = Attendant Console
   </td>
  </tr>
  <tr>
   <td>012
   </td>
   <td>Tenant – 1<sup>st</sup> digit
   </td>
   <td rowspan="2" >Only in 1000 & 2000 (RDS) Feature Packages.  3000 and above, fields are blank.
   </td>
  </tr>
  <tr>
   <td>013
   </td>
   <td>Tenant – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>014
   </td>
   <td>Calling Number – 1
   </td>
   <td rowspan="6" >Information shown in Calling Number fields depends on the Calling Party Identification.  When character 011 is;
<p>
0 – Station number is shown
<p>
1 – Attendant number is shown
   </td>
  </tr>
  <tr>
   <td>015
   </td>
   <td>Calling Number – 2
   </td>
  </tr>
  <tr>
   <td>016
   </td>
   <td>Calling Number – 3
   </td>
  </tr>
  <tr>
   <td>017
   </td>
   <td>Calling Number – 4
   </td>
  </tr>
  <tr>
   <td>018
   </td>
   <td>Calling Number – 5
   </td>
  </tr>
  <tr>
   <td>019
   </td>
   <td>Calling Number – 6
   </td>
  </tr>
  <tr>
   <td>020
   </td>
   <td>Month – Tenths
   </td>
   <td rowspan="10" >Time when SMDR record begins
<p>
For Station-To-Station this time begins when called party answers.
   </td>
  </tr>
  <tr>
   <td>021
   </td>
   <td>Month – Ones
   </td>
  </tr>
  <tr>
   <td>022
   </td>
   <td>Day – Tenths
   </td>
  </tr>
  <tr>
   <td>023
   </td>
   <td>Day – Ones
   </td>
  </tr>
  <tr>
   <td>024
   </td>
   <td>Hour – Tenths
   </td>
  </tr>
  <tr>
   <td>025
   </td>
   <td>Hour – Ones
   </td>
  </tr>
  <tr>
   <td>026
   </td>
   <td>Minute – Tenths
   </td>
  </tr>
  <tr>
   <td>027
   </td>
   <td>Minute – Ones
   </td>
  </tr>
  <tr>
   <td>028
   </td>
   <td>Second – Tenths
   </td>
  </tr>
  <tr>
   <td>029
   </td>
   <td>Second – Ones
   </td>
  </tr>
  <tr>
   <td>030
   </td>
   <td>Month –Tenths
   </td>
   <td rowspan="10" >Time when SMDR record is complete
   </td>
  </tr>
  <tr>
   <td>031
   </td>
   <td>Month – Ones
   </td>
  </tr>
  <tr>
   <td>032
   </td>
   <td>Day – Tenths
   </td>
  </tr>
  <tr>
   <td>033
   </td>
   <td>Day – Ones
   </td>
  </tr>
  <tr>
   <td>034
   </td>
   <td>Hour – Tenths
   </td>
  </tr>
  <tr>
   <td>035
   </td>
   <td>Hour – Ones
   </td>
  </tr>
  <tr>
   <td>036
   </td>
   <td>Minute – Tenths
   </td>
  </tr>
  <tr>
   <td>037
   </td>
   <td>Minute – Ones
   </td>
  </tr>
  <tr>
   <td>038
   </td>
   <td>Second – Tenths
   </td>
  </tr>
  <tr>
   <td>039
   </td>
   <td>Second – Ones
   </td>
  </tr>
  <tr>
   <td>040~049
   </td>
   <td>Blank
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>050
   </td>
   <td>Tenant – 1<sup>st</sup> digit
   </td>
   <td rowspan="3" >Calling Party Tenant Information
<p>
This is for 3000 Series Feature Package and higher.
   </td>
  </tr>
  <tr>
   <td>051
   </td>
   <td>Tenant – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>052
   </td>
   <td>Tenant – 3<sup>rd</sup> digit
   </td>
  </tr>
</table>

<p style="text-align: right">
<strong><span style="text-decoration:underline;">KB Record Cont:</span></strong></p>

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>053
   </td>
   <td>Condition Code One
   </td>
   <td>0 = Call has not transferred
<p>
1 = Call has been transferred
<p>
Example:
<p>
Station-A calls Station-B, talks for 10 minutes then transfers outside to Station-C.  The SMDR record will show Condition 1.
<p>
(<em>Note: ASYD System 1 Index 33 will effect who is billed on a transfer</em>)
   </td>
  </tr>
  <tr>
   <td>054
   </td>
   <td>Condition Code Two
   </td>
   <td>Set to ‘0’
   </td>
  </tr>
  <tr>
   <td>055
   </td>
   <td>Condition Code Three
   </td>
   <td>0 = Regular Outgoing or Tandem call.
<p>
1 = Attendant Operator assisted call.
   </td>
  </tr>
  <tr>
   <td>056~061
   </td>
   <td>Blank
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>062
   </td>
   <td>Called Tenant – 1<sup>st</sup> digit
   </td>
   <td rowspan="2" >Only in 1000 & 2000 (RDS) Feature Packages.  3000 and above, fields are blank.
   </td>
  </tr>
  <tr>
   <td>063
   </td>
   <td>Called Tenant – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>064
   </td>
   <td>Called Number – 1
   </td>
   <td rowspan="6" >Station number that was called.
   </td>
  </tr>
  <tr>
   <td>065
   </td>
   <td>Called Number – 2
   </td>
  </tr>
  <tr>
   <td>066
   </td>
   <td>Called Number – 3
   </td>
  </tr>
  <tr>
   <td>067
   </td>
   <td>Called Number – 4
   </td>
  </tr>
  <tr>
   <td>068
   </td>
   <td>Called Number – 5
   </td>
  </tr>
  <tr>
   <td>069
   </td>
   <td>Called Number – 6
   </td>
  </tr>
  <tr>
   <td>070
   </td>
   <td>Called Tenant – 1<sup>st</sup> digit
   </td>
   <td rowspan="3" >Called Party Tenant Information
<p>
This is for 3000 Series Feature Package and higher.
   </td>
  </tr>
  <tr>
   <td>071
   </td>
   <td>Called Tenant – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>072
   </td>
   <td>Called Tenant – 3<sup>rd</sup> digit
   </td>
  </tr>
  <tr>
   <td>073~093
   </td>
   <td>Blank
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>094~097
   </td>
   <td>0
   </td>
   <td>All set to ‘0’
   </td>
  </tr>
  <tr>
   <td>098~115
   </td>
   <td>Blank
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>116
   </td>
   <td>Year – Tenths
   </td>
   <td rowspan="2" >Year of start of conversation
   </td>
  </tr>
  <tr>
   <td>117
   </td>
   <td>Year – Ones
   </td>
  </tr>
  <tr>
   <td>118
   </td>
   <td>Year – Tenths
   </td>
   <td rowspan="2" >Year of end of conversation
   </td>
  </tr>
  <tr>
   <td>119
   </td>
   <td>Year – Ones
   </td>
  </tr>
  <tr>
   <td>120~130
   </td>
   <td>Blank
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>131
   </td>
   <td>ETX
   </td>
   <td>End of Text
   </td>
  </tr>
</table>

 This page is left blank for your notes**2.2  <span style="text-decoration:underline;">KE Record – Normal Format – Incoming</span>**

    Programming information for this format can be found in Section 1.4

#### Example

    **<span style="text-decoration:underline;">KE Record Cont:</span>**

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>000
   </td>
   <td>STX
   </td>
   <td>Start of Text
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>SA
   </td>
   <td>System Address; fixed data
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>UA
   </td>
   <td>Unit Address
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>Entry Index “K”
   </td>
   <td>“K” = SMDR record
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>Type of Record “E”
   </td>
   <td>“E” = Incoming Call / Normal Format
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Route Number – Hundredths
   </td>
   <td rowspan="6" >Incoming Route and Trunk information
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>Route Number – Tenths
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>Route Number – Ones
   </td>
  </tr>
  <tr>
   <td>008
   </td>
   <td>Trunk Number – Hundredths
   </td>
  </tr>
  <tr>
   <td>009
   </td>
   <td>Trunk Number – Tenths
   </td>
  </tr>
  <tr>
   <td>010
   </td>
   <td>Trunk Number – Ones
   </td>
  </tr>
  <tr>
   <td>011
   </td>
   <td>Called Party Identification
   </td>
   <td>0 = PBX/CTX (DID) station
<p>
1 = Attendant Console
<p>
2 = Incoming Trunk
   </td>
  </tr>
  <tr>
   <td>012
   </td>
   <td>Tenant – 1<sup>st</sup> digit
   </td>
   <td rowspan="2" >Only in 1000 & 2000 (RDS) Feature Packages.  3000 and above, fields are blank.
   </td>
  </tr>
  <tr>
   <td>013
   </td>
   <td>Tenant – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>014
   </td>
   <td>Called Number – 1
   </td>
   <td rowspan="6" >Information shown in Called Number fields depends on the Called Party Identification.  When character 011 is;
<p>
0 – Station number is shown
<p>
1 – Attendant number is shown
<p>
2 – 3 digit Route and Trunk number
   </td>
  </tr>
  <tr>
   <td>015
   </td>
   <td>Called Number – 2
   </td>
  </tr>
  <tr>
   <td>016
   </td>
   <td>Called Number – 3
   </td>
  </tr>
  <tr>
   <td>017
   </td>
   <td>Called Number – 4
   </td>
  </tr>
  <tr>
   <td>018
   </td>
   <td>Called Number – 5
   </td>
  </tr>
  <tr>
   <td>019
   </td>
   <td>Called Number – 6
   </td>
  </tr>
  <tr>
   <td>020
   </td>
   <td>Month – Tenths
   </td>
   <td rowspan="10" >Time when SMDR record begins
<p>
For Station-To-Route the SMDR record begins when Answer Supervision has taken place.  This is effected by ARTD CDN28 or ASYD Index 156 & 157.
   </td>
  </tr>
  <tr>
   <td>021
   </td>
   <td>Month – Ones
   </td>
  </tr>
  <tr>
   <td>022
   </td>
   <td>Day – Tenths
   </td>
  </tr>
  <tr>
   <td>023
   </td>
   <td>Day – Ones
   </td>
  </tr>
  <tr>
   <td>024
   </td>
   <td>Hour – Tenths
   </td>
  </tr>
  <tr>
   <td>025
   </td>
   <td>Hour – Ones
   </td>
  </tr>
  <tr>
   <td>026
   </td>
   <td>Minute – Tenths
   </td>
  </tr>
  <tr>
   <td>027
   </td>
   <td>Minute – Ones
   </td>
  </tr>
  <tr>
   <td>028
   </td>
   <td>Second – Tenths
   </td>
  </tr>
  <tr>
   <td>029
   </td>
   <td>Second – Ones
   </td>
  </tr>
  <tr>
   <td>030
   </td>
   <td>Month –Tenths
   </td>
   <td rowspan="10" >Time when SMDR record is complete
   </td>
  </tr>
  <tr>
   <td>031
   </td>
   <td>Month – Ones
   </td>
  </tr>
  <tr>
   <td>032
   </td>
   <td>Day – Tenths
   </td>
  </tr>
  <tr>
   <td>033
   </td>
   <td>Day – Ones
   </td>
  </tr>
  <tr>
   <td>034
   </td>
   <td>Hour – Tenths
   </td>
  </tr>
  <tr>
   <td>035
   </td>
   <td>Hour – Ones
   </td>
  </tr>
  <tr>
   <td>036
   </td>
   <td>Minute – Tenths
   </td>
  </tr>
  <tr>
   <td>037
   </td>
   <td>Minute – Ones
   </td>
  </tr>
  <tr>
   <td>038
   </td>
   <td>Second – Tenths
   </td>
  </tr>
  <tr>
   <td>039
   </td>
   <td>Second – Ones
   </td>
  </tr>
  <tr>
   <td>040~049
   </td>
   <td>Account Code (max 10 digits)
   </td>
   <td>Blank if Account Code not present
   </td>
  </tr>
  <tr>
   <td>050
   </td>
   <td>Tenant – 1<sup>st</sup> digit
   </td>
   <td rowspan="3" >Called Party Tenant Information
<p>
This is for 3000 Series Feature Package and higher.
   </td>
  </tr>
  <tr>
   <td>051
   </td>
   <td>Tenant – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>052
   </td>
   <td>Tenant – 3<sup>rd</sup> digit
   </td>
  </tr>
</table>

<p style="text-align: right">
<strong><span style="text-decoration:underline;">KE Record Cont:</span></strong></p>

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>053
   </td>
   <td>Condition Code One
   </td>
   <td>0 = Call has not transferred
<p>
1 = Call has been transferred
<p>
Example:
<p>
Station-A calls Station-B, talks for 10 minutes then transfers outside to Station-C.  The SMDR record will show Condition 1.
<p>
(<em>Note: ASYD System 1 Index 33 will effect who is billed on a transfer</em>)
   </td>
  </tr>
  <tr>
   <td>054
   </td>
   <td>Condition Code Two
   </td>
   <td>0 = Incoming, Outgoing, or Tandem call with neither Outgoing Trunk Queuing nor Account Codes used.
<p>
1 = Outgoing Trunk Queuing used, but not Account Codes.
<p>
2 = Account Codes used, but not Outgoing Trunk Queuing.
<p>
3 = Both Outgoing Trunk Queuing and Account Codes used.
   </td>
  </tr>
  <tr>
   <td>055
   </td>
   <td>Condition Code Three
   </td>
   <td>0 = Regular Outgoing or Tandem call.
<p>
1 = Attendant Operator assisted call.
<p>
2 = The call Route Advanced (AOPR).
<p>
3 = Attendant Operator assisted call that Route Advanced.
<p>
4 = Call routed to Least Cost Routing.
<p>
5 = Attendant Operator assisted call that is routed to Least Cost Routing.
   </td>
  </tr>
  <tr>
   <td>056
   </td>
   <td>Selected Route – Hundredths
   </td>
   <td rowspan="3" >Incoming Route Number
   </td>
  </tr>
  <tr>
   <td>057
   </td>
   <td>Selected Route – Tenths
   </td>
  </tr>
  <tr>
   <td>058
   </td>
   <td>Selected Route – Ones
   </td>
  </tr>
  <tr>
   <td>059~061
   </td>
   <td>0
   </td>
   <td>All set to ‘0’
   </td>
  </tr>
  <tr>
   <td>062~093
   </td>
   <td>Blank
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>094~097
   </td>
   <td>0
   </td>
   <td>All set to ‘0’
   </td>
  </tr>
  <tr>
   <td>098~115
   </td>
   <td>CCIS Office Code
<p>
or
<p>
ANI : Calling Party Number
   </td>
   <td>Will show CCIS Office Code (ARNP Rt. 0) when ASYD Index 186 bit 7 = 1.
<p>
Will show ANI when ASYD Index 241
<p>
Bit 4 = 1 & {288, 290, 292, 294} Bit 5 = 0
<p>
(<em>ANI will overwrite CCIS Office Code if it is present</em>)
<p>
<em>ANI is only valid for the KE generated by the ISDN route.  If the ISDN tandems to CCIS, the KE for CCIS will not show ANI.</em>
   </td>
  </tr>
</table>

**<span style="text-decoration:underline;">KE Record Cont:</span>**

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>116
   </td>
   <td>Year – Tenths
   </td>
   <td rowspan="2" >Year of start of conversation
   </td>
  </tr>
  <tr>
   <td>117
   </td>
   <td>Year – Ones
   </td>
  </tr>
  <tr>
   <td>118
   </td>
   <td>Year – Tenths
   </td>
   <td rowspan="2" >Year of end of conversation
   </td>
  </tr>
  <tr>
   <td>119
   </td>
   <td>Year – Ones
   </td>
  </tr>
  <tr>
   <td>120~130
   </td>
   <td>Blank
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>131
   </td>
   <td>ETX
   </td>
   <td>End of text
   </td>
  </tr>
</table>

 **2.3  <span style="text-decoration:underline;">KH Record – Extended Format – Outgoing</span>**

    Programming information for this format can be found in Section 1.4

#### Example

    **<span style="text-decoration:underline;">KH Record Cont:</span>**

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>000
   </td>
   <td>STX
   </td>
   <td>Start of Text
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>0
   </td>
   <td>System Address; fixed data
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>!
   </td>
   <td>Unit Address
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>Entry Index “K”
   </td>
   <td>“K” = SMDR record
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>Type of Record “H”
   </td>
   <td>“H” = Outgoing Call / Extended Format
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Route Number – Hundredths
   </td>
   <td rowspan="6" >Outgoing Route and Trunk information
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>Route Number – Tenths
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>Route Number – Ones
   </td>
  </tr>
  <tr>
   <td>008
   </td>
   <td>Trunk Number – Hundredths
   </td>
  </tr>
  <tr>
   <td>009
   </td>
   <td>Trunk Number – Tenths
   </td>
  </tr>
  <tr>
   <td>010
   </td>
   <td>Trunk Number – Ones
   </td>
  </tr>
  <tr>
   <td>011
   </td>
   <td>Calling Party Identification
   </td>
   <td>0 = PBX/CTX (DID) station
<p>
1 = Attendant Console
<p>
2 = Incoming Trunk
<p>
3 = Monitored Number (<em>Note</em>)
   </td>
  </tr>
  <tr>
   <td>012
   </td>
   <td>Tenant – 1<sup>st</sup> digit
   </td>
   <td rowspan="2" >Only in 1000 & 2000 (RDS) Feature Packages.  3000 and above, fields are blank.
   </td>
  </tr>
  <tr>
   <td>013
   </td>
   <td>Tenant – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>014
   </td>
   <td>Calling Number – 1
   </td>
   <td rowspan="6" >Information shown in Calling Number fields depends on the Calling Party Identification.  When character 011 is;
<p>
0 – Station number is shown
<p>
1 – Attendant number is shown
<p>
2 – 3 digit Route and Trunk number
   </td>
  </tr>
  <tr>
   <td>015
   </td>
   <td>Calling Number – 2
   </td>
  </tr>
  <tr>
   <td>016
   </td>
   <td>Calling Number – 3
   </td>
  </tr>
  <tr>
   <td>017
   </td>
   <td>Calling Number – 4
   </td>
  </tr>
  <tr>
   <td>018
   </td>
   <td>Calling Number – 5
   </td>
  </tr>
  <tr>
   <td>019
   </td>
   <td>Calling Number – 6
   </td>
  </tr>
  <tr>
   <td>020
   </td>
   <td>Month – Tenths
   </td>
   <td rowspan="10" >Time when SMDR record begins
<p>
For Station-To-Route the SMDR record begins when Answer Supervision has taken place.  This is effected by ARTD CDN28 or ASYD Index 156 & 157.
   </td>
  </tr>
  <tr>
   <td>021
   </td>
   <td>Month – Ones
   </td>
  </tr>
  <tr>
   <td>022
   </td>
   <td>Day – Tenths
   </td>
  </tr>
  <tr>
   <td>023
   </td>
   <td>Day – Ones
   </td>
  </tr>
  <tr>
   <td>024
   </td>
   <td>Hour – Tenths
   </td>
  </tr>
  <tr>
   <td>025
   </td>
   <td>Hour – Ones
   </td>
  </tr>
  <tr>
   <td>026
   </td>
   <td>Minute – Tenths
   </td>
  </tr>
  <tr>
   <td>027
   </td>
   <td>Minute – Ones
   </td>
  </tr>
  <tr>
   <td>028
   </td>
   <td>Second – Tenths
   </td>
  </tr>
  <tr>
   <td>029
   </td>
   <td>Second – Ones
   </td>
  </tr>
  <tr>
   <td>030
   </td>
   <td>Month –Tenths
   </td>
   <td rowspan="10" >Time when SMDR record is complete
   </td>
  </tr>
  <tr>
   <td>031
   </td>
   <td>Month – Ones
   </td>
  </tr>
  <tr>
   <td>032
   </td>
   <td>Day – Tenths
   </td>
  </tr>
  <tr>
   <td>033
   </td>
   <td>Day – Ones
   </td>
  </tr>
  <tr>
   <td>034
   </td>
   <td>Hour – Tenths
   </td>
  </tr>
  <tr>
   <td>035
   </td>
   <td>Hour – Ones
   </td>
  </tr>
  <tr>
   <td>036
   </td>
   <td>Minute – Tenths
   </td>
  </tr>
  <tr>
   <td>037
   </td>
   <td>Minute – Ones
   </td>
  </tr>
  <tr>
   <td>038
   </td>
   <td>Second – Tenths
   </td>
  </tr>
  <tr>
   <td>039
   </td>
   <td>Second – Ones
   </td>
  </tr>
  <tr>
   <td>040~049
   </td>
   <td>Account Code (max 10 digits)
   </td>
   <td>Blank if Account Code not present
   </td>
  </tr>
  <tr>
   <td>050
   </td>
   <td>Tenant – 1<sup>st</sup> digit
   </td>
   <td rowspan="3" >Calling Party Tenant Information
<p>
This is for 3000 Series Feature Package and higher.
   </td>
  </tr>
  <tr>
   <td>051
   </td>
   <td>Tenant – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>052
   </td>
   <td>Tenant – 3<sup>rd</sup> digit
   </td>
  </tr>
</table>

_Note: See Appendix D_**<span style="text-decoration:underline;">KH Record Cont:</span>**

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>053
   </td>
   <td>Condition Code One
   </td>
   <td>0 = Call has not transferred
<p>
1 = Call has been transferred
<p>
Example:
<p>
Station-A calls Station-B, talks for 10 minutes then transfers outside to Station-C.  The SMDR record will show Condition 1.
<p>
(<em>Note: ASYD System 1 Index 33 will effect who is billed on a transfer</em>)
   </td>
  </tr>
  <tr>
   <td>054
   </td>
   <td>Condition Code Two
   </td>
   <td>0 = Incoming, Outgoing, or Tandem call with neither Outgoing Trunk Queuing nor Account Codes used.
<p>
1 = Outgoing Trunk Queuing used, but not Account Codes.
<p>
2 = Account Codes used, but not Outgoing Trunk Queuing.
<p>
3 = Both Outgoing Trunk Queuing and Account Codes used.
   </td>
  </tr>
  <tr>
   <td>055
   </td>
   <td>Condition Code Three
   </td>
   <td>0 = Regular Outgoing or Tandem call.
<p>
1 = Attendant Operator assisted call.
<p>
2 = The call Route Advanced (AOPR).
<p>
3 = Attendant Operator assisted call that Route Advanced.
<p>
4 = Call routed to Least Cost Routing.
<p>
5 = Attendant Operator assisted call that is routed to Least Cost Routing.
   </td>
  </tr>
  <tr>
   <td>056
   </td>
   <td>Selected Route – Hundredths
   </td>
   <td rowspan="3" >When Condition Code Three shows 2 through 5, this shows the selected route.
<p>
Otherwise this field blank.
   </td>
  </tr>
  <tr>
   <td>057
   </td>
   <td>Selected Route – Tenths
   </td>
  </tr>
  <tr>
   <td>058
   </td>
   <td>Selected Route – Ones
   </td>
  </tr>
  <tr>
   <td>059
   </td>
   <td>First Route – Hundredths
   </td>
   <td rowspan="3" >When Condition Code Three shows 2 through 5, this shows the First Choice route.  Otherwise this field blank.
<p>
If ASYD System 1, Index 32, Bit 2 = 1 then ARNP for the selected route will be in this field.  If ARNP is set to * then ‘011’ will be here.  If ARNP is set to # then ‘012’ will be here.
   </td>
  </tr>
  <tr>
   <td>060
   </td>
   <td>First Route – Tenths
   </td>
  </tr>
  <tr>
   <td>061
   </td>
   <td>First Route – Ones
   </td>
  </tr>
</table>

**<span style="text-decoration:underline;">KH Record Cont:</span>**

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name and Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>062~085
   </td>
   <td>Called Number (max 32 digits)
   </td>
   <td>If ASYD System 1, Index 32, Bit 5 = 1 then the dialed access code (i.e. 9) is included.
<p>
When ASYD System 1, Index 32, Bit 6 =
<p>
0 – Digits sent are in this field (after AOPR, AADT, etc.)
<p>
1 – Digits dialed are in this field
<p>
When ARTD CDN 121 =
<p>
0 – Digits sent are in this field (after AOPR, AADT, etc.)
<p>
1 – Digits dialed are in this field
<p>
<em>Note: This overrides ASYD above.</em>
   </td>
  </tr>
  <tr>
   <td>086~093
   </td>
   <td>Not Used
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>094
   </td>
   <td>Metering Pulse – Thousands
   </td>
   <td rowspan="4" >When Metering Pulses are received from C.O., they will be in this field.  Default is all ‘0’.
   </td>
  </tr>
  <tr>
   <td>095
   </td>
   <td>Metering Pulse – Hundredths
   </td>
  </tr>
  <tr>
   <td>096
   </td>
   <td>Metering Pulse – Tenths
   </td>
  </tr>
  <tr>
   <td>097
   </td>
   <td>Metering Pulse – Ones
   </td>
  </tr>
  <tr>
   <td>098
   </td>
   <td>Office Code 1 (Digit 1)
   </td>
   <td rowspan="4" >CCIS Office Code from ARNP Route 0 in the Originating PBX.  When ASYD Index 186 Bit 7 = 1
   </td>
  </tr>
  <tr>
   <td>099
   </td>
   <td>Office Code 1 (Digit 2)
   </td>
  </tr>
  <tr>
   <td>100
   </td>
   <td>Office Code 1 (Digit 3)
   </td>
  </tr>
  <tr>
   <td>101
   </td>
   <td>Office Code 1 (Digit 4)
   </td>
  </tr>
  <tr>
   <td>102
   </td>
   <td>Office Code 2 (Digit 1)
   </td>
   <td rowspan="4" >CCIS Office Code from ARNP Route 0 in the Billing PBX (where the call record was created).  When ASYD Index 186 Bit 7 = 1
   </td>
  </tr>
  <tr>
   <td>103
   </td>
   <td>Office Code 2 (Digit 2)
   </td>
  </tr>
  <tr>
   <td>104
   </td>
   <td>Office Code 2 (Digit 3)
   </td>
  </tr>
  <tr>
   <td>105
   </td>
   <td>Office Code 2 (Digit 4)
   </td>
  </tr>
  <tr>
   <td>106~113
   </td>
   <td>Authorization Code
   </td>
   <td>Procedure 2 Auth Code Only
<p>
Max 8 digits
   </td>
  </tr>
  <tr>
   <td>114~115
   </td>
   <td>Blank
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>116
   </td>
   <td>Year – Tenths
   </td>
   <td rowspan="2" >Year of start of conversation
   </td>
  </tr>
  <tr>
   <td>117
   </td>
   <td>Year – Ones
   </td>
  </tr>
  <tr>
   <td>118
   </td>
   <td>Year – Tenths
   </td>
   <td rowspan="2" >Year of end of conversation
   </td>
  </tr>
  <tr>
   <td>119
   </td>
   <td>Year – Ones
   </td>
  </tr>
  <tr>
   <td>120
   </td>
   <td>Set to ‘0’
   </td>
   <td>ISDN Billing indication
   </td>
  </tr>
  <tr>
   <td>121~130
   </td>
   <td>Blank
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>131
   </td>
   <td>ANI
   </td>
   <td>‘A’ = ANI information present
   </td>
  </tr>
  <tr>
   <td>132
   </td>
   <td>ANI Presentation Identifier
   </td>
   <td>0 = No ANI is present
<p>
1 = Displayed
<p>
2 = ANI present, presentation restricted
<p>
3 = Service is not available
<p>
4 = Origination from public pay phone
<p>
5 = Service Condition
   </td>
  </tr>
  <tr>
   <td>133~164
   </td>
   <td>Calling Party Number (ANI)
   </td>
   <td>Max 32 digits
   </td>
  </tr>
  <tr>
   <td>165
   </td>
   <td>Z
   </td>
   <td>End of SMDR information
   </td>
  </tr>
  <tr>
   <td>166
   </td>
   <td>ETX
   </td>
   <td>End of Text
   </td>
  </tr>
</table>

**2.4  <span style="text-decoration:underline;">KI Record – Extended Format – Incoming</span>**

    Programming information for this format can be found in Section 1.4

#### Example

    **<span style="text-decoration:underline;">KI Record Cont:</span>**

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>000
   </td>
   <td>STX
   </td>
   <td>Start of Text
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>0
   </td>
   <td>System Address; fixed data
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>!
   </td>
   <td>Unit Address
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>Entry Index “K”
   </td>
   <td>“K” = SMDR record
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>Type of Record “I”
   </td>
   <td>“I” = Incoming Call / Extended Format
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Route Number – Hundredths
   </td>
   <td rowspan="6" >Incoming Route and Trunk information
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>Route Number – Tenths
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>Route Number – Ones
   </td>
  </tr>
  <tr>
   <td>008
   </td>
   <td>Trunk Number – Hundredths
   </td>
  </tr>
  <tr>
   <td>009
   </td>
   <td>Trunk Number – Tenths
   </td>
  </tr>
  <tr>
   <td>010
   </td>
   <td>Trunk Number – Ones
   </td>
  </tr>
  <tr>
   <td>011
   </td>
   <td>Called Party Identification
   </td>
   <td>0 = PBX/CTX (DID) station
<p>
1 = Attendant Console
<p>
2 = Incoming Trunk
   </td>
  </tr>
  <tr>
   <td>012
   </td>
   <td>Tenant – 1<sup>st</sup> digit
   </td>
   <td rowspan="2" >Only in 1000 & 2000 (RDS) Feature Packages.  3000 and above, fields are blank.
   </td>
  </tr>
  <tr>
   <td>013
   </td>
   <td>Tenant – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>014
   </td>
   <td>Called Number – 1
   </td>
   <td rowspan="6" >Information shown in Called Number fields depends on the Called Party Identification.  When character 011 is;
<p>
0 – Station number is shown
<p>
1 – Attendant number is shown
<p>
2 – 3 digit Route and Trunk number
   </td>
  </tr>
  <tr>
   <td>015
   </td>
   <td>Called Number – 2
   </td>
  </tr>
  <tr>
   <td>016
   </td>
   <td>Called Number – 3
   </td>
  </tr>
  <tr>
   <td>017
   </td>
   <td>Called Number – 4
   </td>
  </tr>
  <tr>
   <td>018
   </td>
   <td>Called Number – 5
   </td>
  </tr>
  <tr>
   <td>019
   </td>
   <td>Called Number – 6
   </td>
  </tr>
  <tr>
   <td>020
   </td>
   <td>Month – Tenths
   </td>
   <td rowspan="10" >Time when SMDR record begins
<p>
For Station-To-Route the SMDR record begins when Answer Supervision has taken place.  This is effected by ARTD CDN28 or ASYD Index 156 & 157.
   </td>
  </tr>
  <tr>
   <td>021
   </td>
   <td>Month – Ones
   </td>
  </tr>
  <tr>
   <td>022
   </td>
   <td>Day – Tenths
   </td>
  </tr>
  <tr>
   <td>023
   </td>
   <td>Day – Ones
   </td>
  </tr>
  <tr>
   <td>024
   </td>
   <td>Hour – Tenths
   </td>
  </tr>
  <tr>
   <td>025
   </td>
   <td>Hour – Ones
   </td>
  </tr>
  <tr>
   <td>026
   </td>
   <td>Minute – Tenths
   </td>
  </tr>
  <tr>
   <td>027
   </td>
   <td>Minute – Ones
   </td>
  </tr>
  <tr>
   <td>028
   </td>
   <td>Second – Tenths
   </td>
  </tr>
  <tr>
   <td>029
   </td>
   <td>Second – Ones
   </td>
  </tr>
  <tr>
   <td>030
   </td>
   <td>Month –Tenths
   </td>
   <td rowspan="10" >Time when SMDR record is complete
   </td>
  </tr>
  <tr>
   <td>031
   </td>
   <td>Month – Ones
   </td>
  </tr>
  <tr>
   <td>032
   </td>
   <td>Day – Tenths
   </td>
  </tr>
  <tr>
   <td>033
   </td>
   <td>Day – Ones
   </td>
  </tr>
  <tr>
   <td>034
   </td>
   <td>Hour – Tenths
   </td>
  </tr>
  <tr>
   <td>035
   </td>
   <td>Hour – Ones
   </td>
  </tr>
  <tr>
   <td>036
   </td>
   <td>Minute – Tenths
   </td>
  </tr>
  <tr>
   <td>037
   </td>
   <td>Minute – Ones
   </td>
  </tr>
  <tr>
   <td>038
   </td>
   <td>Second – Tenths
   </td>
  </tr>
  <tr>
   <td>039
   </td>
   <td>Second – Ones
   </td>
  </tr>
  <tr>
   <td>040~049
   </td>
   <td>Account Code (max 10 digits)
   </td>
   <td>Blank if Account Code not present
   </td>
  </tr>
  <tr>
   <td>050
   </td>
   <td>Tenant – 1<sup>st</sup> digit
   </td>
   <td rowspan="3" >Called Party Tenant Information
<p>
This is for 3000 Series Feature Package and higher.
   </td>
  </tr>
  <tr>
   <td>051
   </td>
   <td>Tenant – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>052
   </td>
   <td>Tenant – 3<sup>rd</sup> digit
   </td>
  </tr>
</table>

<p style="text-align: right">
<strong><span style="text-decoration:underline;">KI Record Cont:</span></strong></p>

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>053
   </td>
   <td>Condition Code One
   </td>
   <td>0 = Call has not transferred
<p>
1 = Call has been transferred
<p>
Example:
<p>
Station-A calls Station-B, talks for 10 minutes then transfers outside to Station-C.  The SMDR record will show Condition 1.
<p>
(<em>Note: ASYD System 1 Index 33 will effect who is billed on a transfer</em>)
   </td>
  </tr>
  <tr>
   <td>054
   </td>
   <td>Condition Code Two
   </td>
   <td>0 = Incoming, Outgoing, or Tandem call with neither Outgoing Trunk Queuing nor Account Codes used.
<p>
1 = Outgoing Trunk Queuing used, but not Account Codes.
<p>
2 = Account Codes used, but not Outgoing Trunk Queuing.
<p>
3 = Both Outgoing Trunk Queuing and Account Codes used.
   </td>
  </tr>
  <tr>
   <td>055
   </td>
   <td>Condition Code Three
   </td>
   <td>0 = Regular Outgoing or Tandem call.
<p>
1 = Attendant Operator assisted call.
<p>
2 = The call Route Advanced (AOPR).
<p>
3 = Attendant Operator assisted call that Route Advanced.
<p>
4 = Call routed to Least Cost Routing.
<p>
5 = Attendant Operator assisted call that is routed to Least Cost Routing.
   </td>
  </tr>
  <tr>
   <td>056
   </td>
   <td>Selected Route – Hundredths
   </td>
   <td rowspan="3" >When Condition Code Three shows 2 through 5, this shows the selected route.
<p>
Otherwise this field blank.
   </td>
  </tr>
  <tr>
   <td>057
   </td>
   <td>Selected Route – Tenths
   </td>
  </tr>
  <tr>
   <td>058
   </td>
   <td>Selected Route – Ones
   </td>
  </tr>
  <tr>
   <td>059~061
   </td>
   <td>0
   </td>
   <td>All set to ‘0’
   </td>
  </tr>
  <tr>
   <td>062~093
   </td>
   <td>Blank
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>094~97
   </td>
   <td>0
   </td>
   <td>All set to ‘0’
   </td>
  </tr>
  <tr>
   <td>098
   </td>
   <td>Office Code 1 (Digit 1)
   </td>
   <td rowspan="4" >CCIS Office Code from ARNP Route 0 in the Originating PBX.  When ASYD Index 186 Bit 7 = 1
   </td>
  </tr>
  <tr>
   <td>099
   </td>
   <td>Office Code 1 (Digit 2)
   </td>
  </tr>
  <tr>
   <td>100
   </td>
   <td>Office Code 1 (Digit 3)
   </td>
  </tr>
  <tr>
   <td>101
   </td>
   <td>Office Code 1 (Digit 4)
   </td>
  </tr>
  <tr>
   <td>102
   </td>
   <td>Office Code 2 (Digit 1)
   </td>
   <td rowspan="4" >CCIS Office Code from ARNP Route 0 in the Billing PBX (where the call record was created).  When ASYD Index 186 Bit 7 = 1
   </td>
  </tr>
  <tr>
   <td>103
   </td>
   <td>Office Code 2 (Digit 2)
   </td>
  </tr>
  <tr>
   <td>104
   </td>
   <td>Office Code 2 (Digit 3)
   </td>
  </tr>
  <tr>
   <td>105
   </td>
   <td>Office Code 2 (Digit 4)
   </td>
  </tr>
  <tr>
   <td>106~115
   </td>
   <td>Blank
   </td>
   <td>
   </td>
  </tr>
</table>

**<span style="text-decoration:underline;">KI Record Cont:</span>**

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>116
   </td>
   <td>Year – Tenths
   </td>
   <td rowspan="2" >Year of start of conversation
   </td>
  </tr>
  <tr>
   <td>117
   </td>
   <td>Year – Ones
   </td>
  </tr>
  <tr>
   <td>118
   </td>
   <td>Year – Tenths
   </td>
   <td rowspan="2" >Year of end of conversation
   </td>
  </tr>
  <tr>
   <td>119
   </td>
   <td>Year – Ones
   </td>
  </tr>
  <tr>
   <td>120~130
   </td>
   <td>Blank
   </td>
   <td>ANI and/or CCIS Office Codes may appear here if ASYD Index 241 Bit 4=1 in Remote Nodes in a CCIS network.
   </td>
  </tr>
  <tr>
   <td>131
   </td>
   <td>ANI
   </td>
   <td>A = ANI Information Present
   </td>
  </tr>
  <tr>
   <td>132
   </td>
   <td>ANI Presentation Identifier
   </td>
   <td>0 = No ANI is present
<p>
1 = Displayed
<p>
2 = ANI present, presentation restricted
<p>
3 = Service is not available
<p>
4 = Origination from public pay phone
<p>
5 = Service Condition
   </td>
  </tr>
  <tr>
   <td>133~161
   </td>
   <td>Calling Party Number (ANI)
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>165
   </td>
   <td>Z
   </td>
   <td>End of SMDR information
   </td>
  </tr>
  <tr>
   <td>166
   </td>
   <td>ETX
   </td>
   <td>End of Text
   </td>
  </tr>
</table>

**2.5  <span style="text-decoration:underline;">KJ Record – Extended Format – Station to Station</span>**

    Programming information for this format can be found in Section 1.4

#### Example

**<span style="text-decoration:underline;">KJ Record Cont:</span>**

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>000
   </td>
   <td>STX
   </td>
   <td>Start of Text
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>0
   </td>
   <td>System Address; fixed data
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>!
   </td>
   <td>Unit Address
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>Entry Index “K”
   </td>
   <td>“K” = SMDR record
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>Type of Record “J”
   </td>
   <td>“J” = Station to Station / Extended Format
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Blank
   </td>
   <td rowspan="6" >
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>Blank
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>Blank
   </td>
  </tr>
  <tr>
   <td>008
   </td>
   <td>Blank
   </td>
  </tr>
  <tr>
   <td>009
   </td>
   <td>Blank
   </td>
  </tr>
  <tr>
   <td>010
   </td>
   <td>Blank
   </td>
  </tr>
  <tr>
   <td>011
   </td>
   <td>Calling Party Identification
   </td>
   <td>0 = PBX/CTX (DID) station
<p>
1 = Attendant Console
<p>
2 = Incoming Trunk
   </td>
  </tr>
  <tr>
   <td>012
   </td>
   <td>Tenant – 1<sup>st</sup> digit
   </td>
   <td rowspan="2" >Only in 1000 & 2000 (RDS) Feature Packages.  3000 and above, fields are blank.
   </td>
  </tr>
  <tr>
   <td>013
   </td>
   <td>Tenant – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>014
   </td>
   <td>Calling Number – 1
   </td>
   <td rowspan="6" >Information shown in Calling Number fields depends on the Calling Party Identification.  When character 011 is;
<p>
0 – Station number is shown
<p>
1 – Attendant number is shown
<p>
2 – 3 digit Route and Trunk number
   </td>
  </tr>
  <tr>
   <td>015
   </td>
   <td>Calling Number – 2
   </td>
  </tr>
  <tr>
   <td>016
   </td>
   <td>Calling Number – 3
   </td>
  </tr>
  <tr>
   <td>017
   </td>
   <td>Calling Number – 4
   </td>
  </tr>
  <tr>
   <td>018
   </td>
   <td>Calling Number – 5
   </td>
  </tr>
  <tr>
   <td>019
   </td>
   <td>Calling Number – 6
   </td>
  </tr>
  <tr>
   <td>020
   </td>
   <td>Month – Tenths
   </td>
   <td rowspan="10" >Time when SMDR record begins
<p>
For Station-To-Route the SMDR record begins when Answer Supervision has taken place.  This is effected by ARTD CDN28 or ASYD Index 156 & 157.
   </td>
  </tr>
  <tr>
   <td>021
   </td>
   <td>Month – Ones
   </td>
  </tr>
  <tr>
   <td>022
   </td>
   <td>Day – Tenths
   </td>
  </tr>
  <tr>
   <td>023
   </td>
   <td>Day – Ones
   </td>
  </tr>
  <tr>
   <td>024
   </td>
   <td>Hour – Tenths
   </td>
  </tr>
  <tr>
   <td>025
   </td>
   <td>Hour – Ones
   </td>
  </tr>
  <tr>
   <td>026
   </td>
   <td>Minute – Tenths
   </td>
  </tr>
  <tr>
   <td>027
   </td>
   <td>Minute – Ones
   </td>
  </tr>
  <tr>
   <td>028
   </td>
   <td>Second – Tenths
   </td>
  </tr>
  <tr>
   <td>029
   </td>
   <td>Second – Ones
   </td>
  </tr>
  <tr>
   <td>030
   </td>
   <td>Month –Tenths
   </td>
   <td rowspan="10" >Time when SMDR record is complete
   </td>
  </tr>
  <tr>
   <td>031
   </td>
   <td>Month – Ones
   </td>
  </tr>
  <tr>
   <td>032
   </td>
   <td>Day – Tenths
   </td>
  </tr>
  <tr>
   <td>033
   </td>
   <td>Day – Ones
   </td>
  </tr>
  <tr>
   <td>034
   </td>
   <td>Hour – Tenths
   </td>
  </tr>
  <tr>
   <td>035
   </td>
   <td>Hour – Ones
   </td>
  </tr>
  <tr>
   <td>036
   </td>
   <td>Minute – Tenths
   </td>
  </tr>
  <tr>
   <td>037
   </td>
   <td>Minute – Ones
   </td>
  </tr>
  <tr>
   <td>038
   </td>
   <td>Second – Tenths
   </td>
  </tr>
  <tr>
   <td>039
   </td>
   <td>Second – Ones
   </td>
  </tr>
  <tr>
   <td>040~049
   </td>
   <td>Account Code (max 10 digits)
   </td>
   <td>Blank if Account Code not present
   </td>
  </tr>
  <tr>
   <td>050
   </td>
   <td>Tenant – 1<sup>st</sup> digit
   </td>
   <td rowspan="3" >Calling Party Tenant Information
<p>
This is for 3000 Series Feature Package and higher.
   </td>
  </tr>
  <tr>
   <td>051
   </td>
   <td>Tenant – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>052
   </td>
   <td>Tenant – 3<sup>rd</sup> digit
   </td>
  </tr>
</table>

<p style="text-align: right">
<strong><span style="text-decoration:underline;">KJ Record Cont:</span></strong></p>

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>053
   </td>
   <td>Condition Code One
   </td>
   <td>0 = Call has not transferred
<p>
1 = Call has been transferred
<p>
Example:
<p>
Station-A calls Station-B, talks for 10 minutes then transfers outside to Station-C.  The SMDR record will show Condition 1.
<p>
(<em>Note: ASYD System 1 Index 33 will effect who is billed on a transfer</em>)
   </td>
  </tr>
  <tr>
   <td>054
   </td>
   <td>Condition Code Two
   </td>
   <td>0 = Incoming, Outgoing, or Tandem call with neither Outgoing Trunk Queuing nor Account Codes used.
<p>
1 = Outgoing Trunk Queuing used, but not Account Codes.
<p>
2 = Account Codes used, but not Outgoing Trunk Queuing.
<p>
3 = Both Outgoing Trunk Queuing and Account Codes used.
   </td>
  </tr>
  <tr>
   <td>055
   </td>
   <td>Condition Code Three
   </td>
   <td>0 = Regular Outgoing or Tandem call.
<p>
1 = Attendant Operator assisted call.
<p>
2 = The call Route Advanced (AOPR).
<p>
3 = Attendant Operator assisted call that Route Advanced.
<p>
4 = Call routed to Least Cost Routing.
<p>
5 = Attendant Operator assisted call that is routed to Least Cost Routing.
   </td>
  </tr>
  <tr>
   <td>056
   </td>
   <td>Selected Route – Hundredths
   </td>
   <td rowspan="3" >When Condition Code Three shows 2 through 5, this shows the selected route.
<p>
Otherwise this field blank.
   </td>
  </tr>
  <tr>
   <td>057
   </td>
   <td>Selected Route – Tenths
   </td>
  </tr>
  <tr>
   <td>058
   </td>
   <td>Selected Route – Ones
   </td>
  </tr>
  <tr>
   <td>059
   </td>
   <td>First Route – Hundredths
   </td>
   <td rowspan="3" >When Condition Code Three shows 2 through 5, this shows the First Choice route.  Otherwise this field blank.
<p>
If ASYD System 1, Index 32, Bit 2 = 1 then ARNP for the selected route will be in this field.  If ARNP is set to * then ‘011’ will be here.  If ARNP is set to # then ‘012’ will be here.
   </td>
  </tr>
  <tr>
   <td>060
   </td>
   <td>First Route – Tenths
   </td>
  </tr>
  <tr>
   <td>061
   </td>
   <td>First Route – Ones
   </td>
  </tr>
</table>

**<span style="text-decoration:underline;">KJ Record Cont:</span>**

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name and Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>062
   </td>
   <td>Called Tenant – 1<sup>st</sup> digit
   </td>
   <td rowspan="2" >Only in 1000 & 2000 (RDS) Feature Packages.  3000 and above, fields are blank.
   </td>
  </tr>
  <tr>
   <td>063
   </td>
   <td>Called Tenant – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>064
   </td>
   <td>Called Number – 1
   </td>
   <td rowspan="6" >Station number that was called.
   </td>
  </tr>
  <tr>
   <td>065
   </td>
   <td>Called Number – 2
   </td>
  </tr>
  <tr>
   <td>066
   </td>
   <td>Called Number – 3
   </td>
  </tr>
  <tr>
   <td>067
   </td>
   <td>Called Number – 4
   </td>
  </tr>
  <tr>
   <td>068
   </td>
   <td>Called Number – 5
   </td>
  </tr>
  <tr>
   <td>069
   </td>
   <td>Called Number – 6
   </td>
  </tr>
  <tr>
   <td>070
   </td>
   <td>Called Tenant – 1<sup>st</sup> digit
   </td>
   <td rowspan="3" >Called Party Tenant Information
<p>
This is for 3000 Series Feature Package and higher.
   </td>
  </tr>
  <tr>
   <td>071
   </td>
   <td>Called Tenant – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>072
   </td>
   <td>Called Tenant – 3<sup>rd</sup> digit
   </td>
  </tr>
  <tr>
   <td>073~093
   </td>
   <td>Blank
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>094~097
   </td>
   <td>0
   </td>
   <td>All set to ‘0’
   </td>
  </tr>
  <tr>
   <td>098~115
   </td>
   <td>Blank
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>116
   </td>
   <td>Year – Tenths
   </td>
   <td rowspan="2" >Year of start of conversation
   </td>
  </tr>
  <tr>
   <td>117
   </td>
   <td>Year – Ones
   </td>
  </tr>
  <tr>
   <td>118
   </td>
   <td>Year – Tenths
   </td>
   <td rowspan="2" >Year of end of conversation
   </td>
  </tr>
  <tr>
   <td>119
   </td>
   <td>Year – Ones
   </td>
  </tr>
  <tr>
   <td>120~130
   </td>
   <td>Blank
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>131
   </td>
   <td>ANI
   </td>
   <td>A = ANI Information Present
   </td>
  </tr>
  <tr>
   <td>132
   </td>
   <td>ANI Presentation Identifier
   </td>
   <td>0 = No ANI is present
<p>
1 = Displayed
<p>
2 = ANI present, presentation restricted
<p>
3 = Service is not available
<p>
4 = Origination from public pay phone
<p>
5 = Service Condition
   </td>
  </tr>
  <tr>
   <td>133~164
   </td>
   <td>Calling Party Number (ANI)
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>165
   </td>
   <td>Z
   </td>
   <td>End of SMDR information
   </td>
  </tr>
  <tr>
   <td>166
   </td>
   <td>ETX
   </td>
   <td>End of Text
   </td>
  </tr>
</table>

**2.6  <span style="text-decoration:underline;">KK Record – IMX Format – Outgoing</span>**

    Programming information for this format can be found in Section 1.4


    The IMX Format is structured in such a fashion as to compress the data stream, maximizing it’s efficiency by elimination of unnecessary gaps in data.  Instead of providing fixed byte sizes for the various fields, the new format provides indexes (i.e. Kind of Data) that will describe the data and length to follow.

#### Valid Data for Outgoing Calls

<table>
  <tr>
   <td><strong>Kind of Data</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td>01
   </td>
   <td>Outgoing Trunk / Incoming Trunk information
   </td>
  </tr>
  <tr>
   <td>02
   </td>
   <td>Calling Party Information (Physical Number)
   </td>
  </tr>
  <tr>
   <td>03
   </td>
   <td>Calling Party Information (Telephone Number)
   </td>
  </tr>
  <tr>
   <td>06
   </td>
   <td>Call Start Time / Call End Time
   </td>
  </tr>
  <tr>
   <td>07
   </td>
   <td>Account Code
   </td>
  </tr>
  <tr>
   <td>08
   </td>
   <td>Condition B Information
   </td>
  </tr>
  <tr>
   <td>09
   </td>
   <td>Alternate Routing Information / Incoming Route Number
   </td>
  </tr>
  <tr>
   <td>10
   </td>
   <td>Dial Code
   </td>
  </tr>
  <tr>
   <td>11
   </td>
   <td>Office Code Information
   </td>
  </tr>
  <tr>
   <td>12
   </td>
   <td>Authorization Code
   </td>
  </tr>
  <tr>
   <td>13
   </td>
   <td>Condition C Information & Billing Information / Call Metering Information
   </td>
  </tr>
  <tr>
   <td>14
   </td>
   <td>Condition D Information & Billing Notification AttCon Number
   </td>
  </tr>
  <tr>
   <td>15
   </td>
   <td>Department Code
   </td>
  </tr>
  <tr>
   <td>17
   </td>
   <td>Change Code
   </td>
  </tr>
</table>

#### Example

**<span style="text-decoration:underline;">KK Record Cont:</span>**

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>000
   </td>
   <td>STX
   </td>
   <td>Start of Text
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>0
   </td>
   <td>System Address; fixed data
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>!
   </td>
   <td>Unit Address
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>Entry Index “K”
   </td>
   <td>“K” = SMDR record
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>Type of Record “K”
   </td>
   <td>“K” = Outgoing Call / IMX Format
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>0
   </td>
   <td rowspan="2" >Kind of Data : 01 Outgoing Trunk
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>1
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>1
   </td>
   <td rowspan="2" >Length of Data = 12 characters
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>2
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>FPC – 1
   </td>
   <td rowspan="3" >Fusion Point Code
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>FPC – 2
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>FPC – 3
   </td>
  </tr>
  <tr>
   <td>008
   </td>
   <td>Physical Route – Hundredths
   </td>
   <td rowspan="3" >Physical Outgoing Route Number (ARTD)
   </td>
  </tr>
  <tr>
   <td>009
   </td>
   <td>Physical Route – Tenths
   </td>
  </tr>
  <tr>
   <td>010
   </td>
   <td>Physical Route – Ones
   </td>
  </tr>
  <tr>
   <td>011
   </td>
   <td>Trunk – Hundredths
   </td>
   <td rowspan="3" >Trunk Number
   </td>
  </tr>
  <tr>
   <td>012
   </td>
   <td>Trunk – Tenths
   </td>
  </tr>
  <tr>
   <td>013
   </td>
   <td>Trunk – Ones
   </td>
  </tr>
  <tr>
   <td>014
   </td>
   <td>Logical Route – Hundredths
   </td>
   <td rowspan="3" >Logical Outgoing Route (ALRTN) if applicable
   </td>
  </tr>
  <tr>
   <td>015
   </td>
   <td>Logical Route – Tenths
   </td>
  </tr>
  <tr>
   <td>016
   </td>
   <td>Logical Route – Ones
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>0
   </td>
   <td rowspan="2" >Kind of Data : 02 Calling Party Information (Physical number)
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>2
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>1
   </td>
   <td rowspan="2" >Length of Data = 10 characters
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Calling Party Identification
   </td>
   <td>0 = PBX/CTX (DID) station
<p>
1 = Attendant Console
<p>
2 = Incoming Trunk
<p>
3 = Monitored Number (<em>Note</em>)
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>Tenant – 1<sup>st</sup> digit
   </td>
   <td rowspan="3" >Calling Party Tenant
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>Tenant – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>008
   </td>
   <td>Tenant – 3<sup>rd</sup> digit
   </td>
  </tr>
  <tr>
   <td>009
   </td>
   <td>Calling Number – 1
   </td>
   <td rowspan="6" >Information shown in Calling Number fields depends on the Calling Party Identification.  When character 011 is;
<p>
0 – Station number is shown
<p>
1 – Attendant number is shown
<p>
2 – 3 digit Route and Trunk number
   </td>
  </tr>
  <tr>
   <td>010
   </td>
   <td>Calling Number – 2
   </td>
  </tr>
  <tr>
   <td>011
   </td>
   <td>Calling Number – 3
   </td>
  </tr>
  <tr>
   <td>012
   </td>
   <td>Calling Number – 4
   </td>
  </tr>
  <tr>
   <td>013
   </td>
   <td>Calling Number – 5
   </td>
  </tr>
  <tr>
   <td>014
   </td>
   <td>Calling Number – 6
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>0
   </td>
   <td rowspan="2" >Kind of Data : 03 Calling Party Number (Telephone Number)
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>3
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>
   </td>
   <td rowspan="2" >Length of Data : Variable 3 to 22
<p>
                           03 when no data
<p>
                           22 maximum
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Fusion Point Code – 1
   </td>
   <td rowspan="3" >Fusion Point Code : If no Fusion Point Code present then these fields will be set to ‘0’
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>Fusion Point Code – 2
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>Fusion Point Code – 3
   </td>
  </tr>
  <tr>
   <td>008
   </td>
   <td>User Group – 1
   </td>
   <td rowspan="3" >Fusion User Group Number
   </td>
  </tr>
  <tr>
   <td>009
   </td>
   <td>User Group – 2
   </td>
  </tr>
  <tr>
   <td>010
   </td>
   <td>User Group – 3
   </td>
  </tr>
  <tr>
   <td>011~026
   </td>
   <td>Calling Party Number
   </td>
   <td>Calling Party Number (logical ; 16 digits)
   </td>
  </tr>
</table>

_Note: See Appendix D_**<span style="text-decoration:underline;">KK Record Cont:</span>**

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>0
   </td>
   <td rowspan="2" >Kind of Data : 06 Call Start / End Time
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>6
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>3
   </td>
   <td rowspan="2" >Length of Data : 34 characters
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>4
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Year – Thousandths
   </td>
   <td rowspan="4" >Call Start : Year
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>Year – Hundredths
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>Year – Tenths
   </td>
  </tr>
  <tr>
   <td>008
   </td>
   <td>Year – Ones
   </td>
  </tr>
  <tr>
   <td>009
   </td>
   <td>Month – Tenths
   </td>
   <td rowspan="2" >Call Start : Month
   </td>
  </tr>
  <tr>
   <td>010
   </td>
   <td>Month – Ones
   </td>
  </tr>
  <tr>
   <td>011
   </td>
   <td>Day – Tenths
   </td>
   <td rowspan="2" >Call Start : Day
   </td>
  </tr>
  <tr>
   <td>012
   </td>
   <td>Day – Ones
   </td>
  </tr>
  <tr>
   <td>013
   </td>
   <td>Hour – Tenths
   </td>
   <td rowspan="2" >Call Start : Hour
   </td>
  </tr>
  <tr>
   <td>014
   </td>
   <td>Hour – Ones
   </td>
  </tr>
  <tr>
   <td>015
   </td>
   <td>Minute – Tenths
   </td>
   <td rowspan="2" >Call Start : Minute
   </td>
  </tr>
  <tr>
   <td>016
   </td>
   <td>Minute – Ones
   </td>
  </tr>
  <tr>
   <td>017
   </td>
   <td>Second – Tenths
   </td>
   <td rowspan="2" >Call Start : Second
   </td>
  </tr>
  <tr>
   <td>018
   </td>
   <td>Second – Ones
   </td>
  </tr>
  <tr>
   <td>019
   </td>
   <td>Milli-Second – Hundredths
   </td>
   <td rowspan="3" >Call Start : Milli-Second
   </td>
  </tr>
  <tr>
   <td>020
   </td>
   <td>Milli-Second – Tenths
   </td>
  </tr>
  <tr>
   <td>021
   </td>
   <td>Milli-Second – Ones
   </td>
  </tr>
  <tr>
   <td>022
   </td>
   <td>Year – Thousandths
   </td>
   <td rowspan="4" >Call End : Year
   </td>
  </tr>
  <tr>
   <td>023
   </td>
   <td>Year – Hundredths
   </td>
  </tr>
  <tr>
   <td>024
   </td>
   <td>Year – Tenths
   </td>
  </tr>
  <tr>
   <td>025
   </td>
   <td>Year – Ones
   </td>
  </tr>
  <tr>
   <td>026
   </td>
   <td>Month – Tenths
   </td>
   <td rowspan="2" >Call End : Month
   </td>
  </tr>
  <tr>
   <td>027
   </td>
   <td>Month – Ones
   </td>
  </tr>
  <tr>
   <td>028
   </td>
   <td>Day – Tenths
   </td>
   <td rowspan="2" >Call End : Day
   </td>
  </tr>
  <tr>
   <td>029
   </td>
   <td>Day – Ones
   </td>
  </tr>
  <tr>
   <td>030
   </td>
   <td>Hour – Tenths
   </td>
   <td rowspan="2" >Call End : Hour
   </td>
  </tr>
  <tr>
   <td>031
   </td>
   <td>Hour – Ones
   </td>
  </tr>
  <tr>
   <td>032
   </td>
   <td>Minute – Tenths
   </td>
   <td rowspan="2" >Call End : Minute
   </td>
  </tr>
  <tr>
   <td>033
   </td>
   <td>Minute – Ones
   </td>
  </tr>
  <tr>
   <td>034
   </td>
   <td>Second – Tenths
   </td>
   <td rowspan="2" >Call End : Second
   </td>
  </tr>
  <tr>
   <td>035
   </td>
   <td>Second – Ones
   </td>
  </tr>
  <tr>
   <td>036
   </td>
   <td>Milli-Second – Hundredths
   </td>
   <td rowspan="3" >Call End : Milli-Second
   </td>
  </tr>
  <tr>
   <td>037
   </td>
   <td>Milli-Second – Tenths
   </td>
  </tr>
  <tr>
   <td>038
   </td>
   <td>Milli-Second – Ones
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>0
   </td>
   <td rowspan="2" >Kind of Data : 07 Account Code
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>7
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>
   </td>
   <td rowspan="2" >Length of Data : Variable 1 to 16
<p>
                           01 when no data
<p>
                          16 maximum
<p>
(<em>ASYDL Index 805 can increase the maximum to 24</em>)
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>005~020
   </td>
   <td>Account Code
   </td>
   <td>Account Code max 16 digits
<p>
(<em>ASYDL Index 805 can increase the maximum to 24</em>)
   </td>
  </tr>
</table>

**<span style="text-decoration:underline;">KK Record Cont:</span>**

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>0
   </td>
   <td rowspan="2" >Kind of Data : 08 Condition Codes
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>8
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>0
   </td>
   <td rowspan="2" >Length of Data : 3 characters
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>3
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Condition Code Zero (C0)
   </td>
   <td>0 = <em>No Condition</em>
<p>
1 = Call was transferred
<p>
2 = Billing is continued
<p>
3 = Call was transferred & Billing is
<p>
      continued
<p>
4 = Call was transferred to last called
<p>
      party
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>Condition Code One (C1)
   </td>
   <td>Call Origination is:
<p>
0 = <em>No Condition</em>
<p>
1 = by OG Queuing
<p>
2 = by dialing with Account Code
<p>
3 = by OG Queuing & dialing with Account
<p>
      Code
<p>
4 = by Forward Outside
<p>
5 = <em>Not Used</em>
<p>
6 = by Forward Outside & dialing with
<p>
      Account Code
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>Condition Code Two (C2)
   </td>
   <td>Call Origination is:
<p>
0 = Direct
<p>
1 = via Att Con
<p>
2 = Direct (Alternate Routing)
<p>
3 = via Att Con (Alternate Routing)
<p>
4 = Direct (LCR Routing)
<p>
5 = via Att Con (LCR Routing)
<p>
6 = Direct (Called number = first 6 digits of
<p>
      change code)
<p>
7 = via Att Con (Called number = first 6
<p>
      digits of change code)
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>0
   </td>
   <td rowspan="2" >Kind of Data : 09 Alternate Routing
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>9
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>1
   </td>
   <td rowspan="2" >Length of Data : 18 characters
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>8
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Fusion Point Code – 1<sup>st</sup> digit
   </td>
   <td rowspan="3" >Fusion Point Code that was used
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>Fusion Point Code – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>Fusion Point Code – 3<sup>rd</sup> digit
   </td>
  </tr>
  <tr>
   <td>008
   </td>
   <td>Route Number – Hundredths
   </td>
   <td rowspan="3" >Physical Route Number that was used
   </td>
  </tr>
  <tr>
   <td>009
   </td>
   <td>Route Number – Tenths
   </td>
  </tr>
  <tr>
   <td>010
   </td>
   <td>Route Number – Ones
   </td>
  </tr>
  <tr>
   <td>011
   </td>
   <td>Route Number – Hundredths
   </td>
   <td rowspan="3" >Logical Route Number that was used
   </td>
  </tr>
  <tr>
   <td>012
   </td>
   <td>Route Number – Tenths
   </td>
  </tr>
  <tr>
   <td>013
   </td>
   <td>Route Number – Ones
   </td>
  </tr>
  <tr>
   <td>014
   </td>
   <td>Fusion Point Code – 1<sup>st</sup> digit
   </td>
   <td rowspan="3" >Fusion Point Code which was first selected
   </td>
  </tr>
  <tr>
   <td>015
   </td>
   <td>Fusion Point Code – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>016
   </td>
   <td>Fusion Point Code – 3<sup>rd</sup> digit
   </td>
  </tr>
  <tr>
   <td>017
   </td>
   <td>Route Number – Hundredths
   </td>
   <td rowspan="3" >Physical Route Number which was first selected
   </td>
  </tr>
  <tr>
   <td>018
   </td>
   <td>Route Number – Tenths
   </td>
  </tr>
  <tr>
   <td>019
   </td>
   <td>Route Number – Ones
   </td>
  </tr>
</table>

<p style="text-align: right">
<strong><span style="text-decoration:underline;">KK Record Cont:</span></strong></p>

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>120
   </td>
   <td>Route Number – Hundredths
   </td>
   <td rowspan="3" >Logical Route Number which was first selected
   </td>
  </tr>
  <tr>
   <td>121
   </td>
   <td>Route Number – Tenths
   </td>
  </tr>
  <tr>
   <td>122
   </td>
   <td>Route Number – Ones
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>1
   </td>
   <td rowspan="2" >Kind of data : 10 Dialed Number
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>
   </td>
   <td rowspan="2" >Length of Data : Variable 1 to 32
<p>
                           01 when no data
<p>
                           32 maximum
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>005~037
   </td>
   <td>Number Dialed (sent?)
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>1
   </td>
   <td rowspan="2" >Kind of Data : 11 Office Code Information
<p>
                      (May be omitted)
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>1
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>0
   </td>
   <td rowspan="2" >Length of Data : 8 characters
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>8
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Office Code – 1<sup>st</sup> digit
   </td>
   <td rowspan="4" >Office Code of Calling Party
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>Office Code – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>Office Code – 3<sup>rd</sup> digit
   </td>
  </tr>
  <tr>
   <td>008
   </td>
   <td>Office Code – 4<sup>th</sup> digit
   </td>
  </tr>
  <tr>
   <td>009
   </td>
   <td>Office Code – 1<sup>st</sup> digit
   </td>
   <td rowspan="4" >Office Code of Billing Process Office
   </td>
  </tr>
  <tr>
   <td>010
   </td>
   <td>Office Code – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>011
   </td>
   <td>Office Code – 3<sup>rd</sup> digit
   </td>
  </tr>
  <tr>
   <td>012
   </td>
   <td>Office Code – 4<sup>th</sup> digit
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>1
   </td>
   <td rowspan="2" >Kind of Data : 12 Authorization Code
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>2
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>
   </td>
   <td rowspan="2" >Length of Data : Variable 1 to 16
<p>
                          01 when no data ?
<p>
                          16 maximum
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>005~020
   </td>
   <td>Authorization Code
   </td>
   <td>Max 16 digits
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>1
   </td>
   <td rowspan="2" >Kind of Data : 13 Call Metering Info
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>3
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>
   </td>
   <td rowspan="2" >Length of Data : Variable 1 to 7
<p>
                           01 when no data
<p>
                           07 maximum
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Charge Information
   </td>
   <td>0 = No Charge Information
<p>
1 = 1 cent unit
<p>
2 = 0.1 cent unit
<p>
3 = 10 cent unit
<p>
4 = $1 unit
<p>
5 = $10 unit
<p>
6 = Calling Metering (4 digits)
<p>
F = Charge Information Error
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td colspan="2" >Charge Data (Basic Charge Unit x 10<sup>0</sup>)
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td colspan="2" >Charge Data (Basic Charge Unit x 10<sup>1</sup>)
   </td>
  </tr>
  <tr>
   <td>008
   </td>
   <td colspan="2" >Charge Data (Basic Charge Unit x 10<sup>2</sup>)
   </td>
  </tr>
  <tr>
   <td>009
   </td>
   <td colspan="2" >Charge Data (Basic Charge Unit x 10<sup>3</sup>)
   </td>
  </tr>
  <tr>
   <td>010
   </td>
   <td colspan="2" >Charge Data (Basic Charge Unit x 10<sup>4</sup>)
   </td>
  </tr>
  <tr>
   <td>011
   </td>
   <td colspan="2" >Charge Data (Basic Charge Unit x 10<sup>5</sup>)
   </td>
  </tr>
</table>

**<span style="text-decoration:underline;">KK Record Cont:</span>**

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>1
   </td>
   <td rowspan="2" >Kind of Data : 14 Bill Notification Att Con
<p>
                       Number (May be omitted)
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>4
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>
   </td>
   <td rowspan="2" >Length of Data : Variable 1 to 4
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Bill Notification by Attendant Console
   </td>
   <td>Blank = Not Available
<p>
0 = Not Applied
<p>
1 = Available
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>Att Con Number – 1<sup>st</sup> digit
   </td>
   <td rowspan="3" >
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>Att Con Number – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>008
   </td>
   <td>Att Con Number – 3<sup>rd</sup> digit
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>1
   </td>
   <td rowspan="2" >Kind of Data : 15 Department Code
<p>
                       (May be omitted)
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>5
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>0
   </td>
   <td rowspan="2" >Length of Data : 3 characters
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>3
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Department Code – 1<sup>st</sup> digit
   </td>
   <td rowspan="3" >
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>Department Code – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>Department Code – 3<sup>rd</sup> digit
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>1
   </td>
   <td rowspan="2" >Kind of Data : 17 Change Code
<p>
                       (May be omitted)
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>7
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>
   </td>
   <td rowspan="2" >Length of Data : Variable 1 to 32
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>005~036
   </td>
   <td>Change Code
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>ETX
   </td>
   <td>End of Text
   </td>
  </tr>
</table>

**2.7  <span style="text-decoration:underline;">KL Record – IMX Format – Incoming</span>**

    Programming information for this format can be found in Section 1.4


    The IMX Format is structured in such a fashion as to compress the data stream, maximizing it’s efficiency by elimination of unnecessary gaps in data.  Instead of providing fixed byte sizes for the various fields, the new format provides indexes (i.e. Kind of Data) that will describe the data and length to follow.

#### Valid Data for Outgoing Calls

<table>
  <tr>
   <td><strong>Kind of Data</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td>01
   </td>
   <td>Outgoing Trunk / Incoming Trunk information
   </td>
  </tr>
  <tr>
   <td>04
   </td>
   <td>Called Party Information (Physical Number)
   </td>
  </tr>
  <tr>
   <td>05
   </td>
   <td>Called Party Information (Telephone Number)
   </td>
  </tr>
  <tr>
   <td>06
   </td>
   <td>Call Start Time / Call End Time
   </td>
  </tr>
  <tr>
   <td>07
   </td>
   <td>Account Code
   </td>
  </tr>
  <tr>
   <td>08
   </td>
   <td>Condition B Information
   </td>
  </tr>
  <tr>
   <td>09
   </td>
   <td>Alternate Routing Information / Incoming Route Number
   </td>
  </tr>
  <tr>
   <td>10
   </td>
   <td>Dial Code
   </td>
  </tr>
  <tr>
   <td>11
   </td>
   <td>Office Code Information
   </td>
  </tr>
  <tr>
   <td>13
   </td>
   <td>Condition C Information & Billing Information / Call Metering Information
   </td>
  </tr>
  <tr>
   <td>16
   </td>
   <td>Calling Station Number
   </td>
  </tr>
  <tr>
   <td>17
   </td>
   <td>Change Code
   </td>
  </tr>
</table>

#### Example

    **<span style="text-decoration:underline;">KL Record Cont:</span>**

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>000
   </td>
   <td>STX
   </td>
   <td>Start of Text
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>0
   </td>
   <td>System Address; fixed data
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>!
   </td>
   <td>Unit Address
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>Entry Index “K”
   </td>
   <td>“K” = SMDR record
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>Type of Record “K”
   </td>
   <td>“L” = Incoming Call / IMX Format
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>0
   </td>
   <td rowspan="2" >Kind of Data : 01 Incoming Trunk
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>1
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>1
   </td>
   <td rowspan="2" >Length of Data = 12 characters
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>2
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>FPC – 1
   </td>
   <td rowspan="3" >Fusion Point Code
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>FPC – 2
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>FPC – 3
   </td>
  </tr>
  <tr>
   <td>008
   </td>
   <td>Physical Route – Hundredths
   </td>
   <td rowspan="3" >Physical Incoming Route Number (ARTD)
   </td>
  </tr>
  <tr>
   <td>009
   </td>
   <td>Physical Route – Tenths
   </td>
  </tr>
  <tr>
   <td>010
   </td>
   <td>Physical Route – Ones
   </td>
  </tr>
  <tr>
   <td>011
   </td>
   <td>Trunk – Hundredths
   </td>
   <td rowspan="3" >Trunk Number
   </td>
  </tr>
  <tr>
   <td>012
   </td>
   <td>Trunk – Tenths
   </td>
  </tr>
  <tr>
   <td>013
   </td>
   <td>Trunk – Ones
   </td>
  </tr>
  <tr>
   <td>014
   </td>
   <td>Logical Route – Hundredths
   </td>
   <td rowspan="3" >Logical Incoming Route (ALRTN) if applicable
   </td>
  </tr>
  <tr>
   <td>015
   </td>
   <td>Logical Route – Tenths
   </td>
  </tr>
  <tr>
   <td>016
   </td>
   <td>Logical Route – Ones
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>0
   </td>
   <td rowspan="2" >Kind of Data : 04 Called Party Information (Physical number)
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>4
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>1
   </td>
   <td rowspan="2" >Length of Data = 10 characters
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Calling Party Identification
   </td>
   <td>0 = PBX/CTX (DID) station
<p>
1 = Attendant Console
<p>
2 = Incoming Trunk
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>Tenant – 1<sup>st</sup> digit
   </td>
   <td rowspan="3" >Called Party Tenant
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>Tenant – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>008
   </td>
   <td>Tenant – 3<sup>rd</sup> digit
   </td>
  </tr>
  <tr>
   <td>009
   </td>
   <td>Calling Number – 1
   </td>
   <td rowspan="6" >Information shown in Called Number fields depends on the Called Party Identification.  When character 011 is;
<p>
0 – Station number is shown
<p>
1 – Attendant number is shown
<p>
2 – 3 digit Route and Trunk number
   </td>
  </tr>
  <tr>
   <td>010
   </td>
   <td>Calling Number – 2
   </td>
  </tr>
  <tr>
   <td>011
   </td>
   <td>Calling Number – 3
   </td>
  </tr>
  <tr>
   <td>012
   </td>
   <td>Calling Number – 4
   </td>
  </tr>
  <tr>
   <td>013
   </td>
   <td>Calling Number – 5
   </td>
  </tr>
  <tr>
   <td>014
   </td>
   <td>Calling Number – 6
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>0
   </td>
   <td rowspan="2" >Kind of Data : 05 Called Party Number (Telephone Number)
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>5
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>
   </td>
   <td rowspan="2" >Length of Data : Variable 3 to 22
<p>
                           03 when no data
<p>
                           22 maximum
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Fusion Point Code – 1
   </td>
   <td rowspan="3" >Fusion Point Code : If no Fusion Point Code present then these fields will be set to ‘0’
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>Fusion Point Code – 2
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>Fusion Point Code – 3
   </td>
  </tr>
  <tr>
   <td>008
   </td>
   <td>User Group – 1
   </td>
   <td rowspan="3" >Fusion User Group Number
   </td>
  </tr>
  <tr>
   <td>009
   </td>
   <td>User Group – 2
   </td>
  </tr>
  <tr>
   <td>010
   </td>
   <td>User Group – 3
   </td>
  </tr>
  <tr>
   <td>011~026
   </td>
   <td>Calling Party Number
   </td>
   <td>Called Party Number (logical ; 16 digits)
   </td>
  </tr>
</table>

<p style="text-align: right">
<strong><span style="text-decoration:underline;">KL Record Cont:</span></strong></p>

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>0
   </td>
   <td rowspan="2" >Kind of Data : 06 Call Start / End Time
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>6
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>3
   </td>
   <td rowspan="2" >Length of Data : 34 characters
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>4
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Year – Thousandths
   </td>
   <td rowspan="4" >Call Start : Year
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>Year – Hundredths
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>Year – Tenths
   </td>
  </tr>
  <tr>
   <td>008
   </td>
   <td>Year – Ones
   </td>
  </tr>
  <tr>
   <td>009
   </td>
   <td>Month – Tenths
   </td>
   <td rowspan="2" >Call Start : Month
   </td>
  </tr>
  <tr>
   <td>010
   </td>
   <td>Month – Ones
   </td>
  </tr>
  <tr>
   <td>011
   </td>
   <td>Day – Tenths
   </td>
   <td rowspan="2" >Call Start : Day
   </td>
  </tr>
  <tr>
   <td>012
   </td>
   <td>Day – Ones
   </td>
  </tr>
  <tr>
   <td>013
   </td>
   <td>Hour – Tenths
   </td>
   <td rowspan="2" >Call Start : Hour
   </td>
  </tr>
  <tr>
   <td>014
   </td>
   <td>Hour – Ones
   </td>
  </tr>
  <tr>
   <td>015
   </td>
   <td>Minute – Tenths
   </td>
   <td rowspan="2" >Call Start : Minute
   </td>
  </tr>
  <tr>
   <td>016
   </td>
   <td>Minute – Ones
   </td>
  </tr>
  <tr>
   <td>017
   </td>
   <td>Second – Tenths
   </td>
   <td rowspan="2" >Call Start : Second
   </td>
  </tr>
  <tr>
   <td>018
   </td>
   <td>Second – Ones
   </td>
  </tr>
  <tr>
   <td>019
   </td>
   <td>Milli-Second – Hundredths
   </td>
   <td rowspan="3" >Call Start : Milli-Second
   </td>
  </tr>
  <tr>
   <td>020
   </td>
   <td>Milli-Second – Tenths
   </td>
  </tr>
  <tr>
   <td>021
   </td>
   <td>Milli-Second – Ones
   </td>
  </tr>
  <tr>
   <td>022
   </td>
   <td>Year – Thousandths
   </td>
   <td rowspan="4" >Call End : Year
   </td>
  </tr>
  <tr>
   <td>023
   </td>
   <td>Year – Hundredths
   </td>
  </tr>
  <tr>
   <td>024
   </td>
   <td>Year – Tenths
   </td>
  </tr>
  <tr>
   <td>025
   </td>
   <td>Year – Ones
   </td>
  </tr>
  <tr>
   <td>026
   </td>
   <td>Month – Tenths
   </td>
   <td rowspan="2" >Call End : Month
   </td>
  </tr>
  <tr>
   <td>027
   </td>
   <td>Month – Ones
   </td>
  </tr>
  <tr>
   <td>028
   </td>
   <td>Day – Tenths
   </td>
   <td rowspan="2" >Call End : Day
   </td>
  </tr>
  <tr>
   <td>029
   </td>
   <td>Day – Ones
   </td>
  </tr>
  <tr>
   <td>030
   </td>
   <td>Hour – Tenths
   </td>
   <td rowspan="2" >Call End : Hour
   </td>
  </tr>
  <tr>
   <td>031
   </td>
   <td>Hour – Ones
   </td>
  </tr>
  <tr>
   <td>032
   </td>
   <td>Minute – Tenths
   </td>
   <td rowspan="2" >Call End : Minute
   </td>
  </tr>
  <tr>
   <td>033
   </td>
   <td>Minute – Ones
   </td>
  </tr>
  <tr>
   <td>034
   </td>
   <td>Second – Tenths
   </td>
   <td rowspan="2" >Call End : Second
   </td>
  </tr>
  <tr>
   <td>035
   </td>
   <td>Second – Ones
   </td>
  </tr>
  <tr>
   <td>036
   </td>
   <td>Milli-Second – Hundredths
   </td>
   <td rowspan="3" >Call End : Milli-Second
   </td>
  </tr>
  <tr>
   <td>037
   </td>
   <td>Milli-Second – Tenths
   </td>
  </tr>
  <tr>
   <td>038
   </td>
   <td>Milli-Second – Ones
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>0
   </td>
   <td rowspan="2" >Kind of Data : 07 Account Code
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>7
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>
   </td>
   <td rowspan="2" >Length of Data : Variable 1 to 16
<p>
                           01 when no data
<p>
                          16 maximum
<p>
(<em>ASYDL Index 805 can increase the maximum to 24</em>)
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>005~020
   </td>
   <td>Account Code
   </td>
   <td>Account Code max 16 digits
<p>
(<em>ASYDL Index 805 can increase the maximum to 24</em>)
   </td>
  </tr>
</table>

**<span style="text-decoration:underline;">KL Record Cont:</span>**

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>0
   </td>
   <td rowspan="2" >Kind of Data : 08 Condition Codes
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>8
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>0
   </td>
   <td rowspan="2" >Length of Data : 3 characters
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>3
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Condition Code Zero (C0)
   </td>
   <td>0 = <em>No Condition</em>
<p>
1 = Call was transferred
<p>
2 = Billing is continued
<p>
3 = Call was transferred & Billing is
<p>
      continued
<p>
4 = Call was transferred to last called
<p>
      party
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>Condition Code One (C1)
   </td>
   <td>Call Origination is:
<p>
0 = <em>No Condition</em>
<p>
1 = by OG Queuing
<p>
2 = by dialing with Account Code
<p>
3 = by OG Queuing & dialing with Account
<p>
      Code
<p>
4 = by Forward Outside
<p>
5 = <em>Not Used</em>
<p>
6 = by Forward Outside & dialing with
<p>
      Account Code
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>Condition Code Two (C2)
   </td>
   <td>Call Origination is:
<p>
0 = Direct
<p>
1 = via Att Con
<p>
2 = Direct (Alternate Routing)
<p>
3 = via Att Con (Alternate Routing)
<p>
4 = Direct (LCR Routing)
<p>
5 = via Att Con (LCR Routing)
<p>
6 = Direct (Called number = first 6 digits of
<p>
      change code)
<p>
7 = via Att Con (Called number = first 6
<p>
      digits of change code)
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>0
   </td>
   <td rowspan="2" >Kind of Data : 09 Alternate Routing
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>9
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>1
   </td>
   <td rowspan="2" >Length of Data : 18 characters
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>8
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Fusion Point Code – 1<sup>st</sup> digit
   </td>
   <td rowspan="3" >Fusion Point Code that was used
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>Fusion Point Code – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>Fusion Point Code – 3<sup>rd</sup> digit
   </td>
  </tr>
  <tr>
   <td>008
   </td>
   <td>Route Number – Hundredths
   </td>
   <td rowspan="3" >Physical Route Number that was used
   </td>
  </tr>
  <tr>
   <td>009
   </td>
   <td>Route Number – Tenths
   </td>
  </tr>
  <tr>
   <td>010
   </td>
   <td>Route Number – Ones
   </td>
  </tr>
  <tr>
   <td>011
   </td>
   <td>Route Number – Hundredths
   </td>
   <td rowspan="3" >Logical Route Number that was used
   </td>
  </tr>
  <tr>
   <td>012
   </td>
   <td>Route Number – Tenths
   </td>
  </tr>
  <tr>
   <td>013
   </td>
   <td>Route Number – Ones
   </td>
  </tr>
  <tr>
   <td>014
   </td>
   <td>Fusion Point Code – 1<sup>st</sup> digit
   </td>
   <td rowspan="3" >Fusion Point Code which was first selected
   </td>
  </tr>
  <tr>
   <td>015
   </td>
   <td>Fusion Point Code – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>016
   </td>
   <td>Fusion Point Code – 3<sup>rd</sup> digit
   </td>
  </tr>
  <tr>
   <td>017
   </td>
   <td>Route Number – Hundredths
   </td>
   <td rowspan="3" >Physical Route Number which was first selected
   </td>
  </tr>
  <tr>
   <td>018
   </td>
   <td>Route Number – Tenths
   </td>
  </tr>
  <tr>
   <td>019
   </td>
   <td>Route Number – Ones
   </td>
  </tr>
</table>

<p style="text-align: right">
<strong><span style="text-decoration:underline;">KL Record Cont:</span></strong></p>

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td colspan="2" ><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>120
   </td>
   <td>Route Number – Hundredths
   </td>
   <td rowspan="3" colspan="2" >Logical Route Number which was first selected
   </td>
  </tr>
  <tr>
   <td>121
   </td>
   <td>Route Number – Tenths
   </td>
  </tr>
  <tr>
   <td>122
   </td>
   <td>Route Number – Ones
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>1
   </td>
   <td rowspan="2" colspan="2" >Kind of data : 10 Dialed Number
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>
   </td>
   <td rowspan="2" colspan="2" >Length of Data : Variable 1 to 32
<p>
                           01 when no data
<p>
                           32 maximum
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>005~037
   </td>
   <td>Number Dialed (sent?)
   </td>
   <td colspan="2" >
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>1
   </td>
   <td rowspan="2" colspan="2" >Kind of Data : 11 Office Code Information
<p>
                      (May be omitted)
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>1
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>0
   </td>
   <td rowspan="2" colspan="2" >Length of Data : 8 characters
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>8
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Office Code – 1<sup>st</sup> digit
   </td>
   <td rowspan="4" colspan="2" >Office Code of Calling Party
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>Office Code – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>Office Code – 3<sup>rd</sup> digit
   </td>
  </tr>
  <tr>
   <td>008
   </td>
   <td>Office Code – 4<sup>th</sup> digit
   </td>
  </tr>
  <tr>
   <td>009
   </td>
   <td>Office Code – 1<sup>st</sup> digit
   </td>
   <td rowspan="4" colspan="2" >Office Code of Billing Process Office
   </td>
  </tr>
  <tr>
   <td>010
   </td>
   <td>Office Code – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>011
   </td>
   <td>Office Code – 3<sup>rd</sup> digit
   </td>
  </tr>
  <tr>
   <td>012
   </td>
   <td>Office Code – 4<sup>th</sup> digit
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>1
   </td>
   <td rowspan="2" colspan="2" >Kind of Data : 13 Call Metering Info
<p>
                       (May be omitted)
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>3
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>
   </td>
   <td rowspan="2" colspan="2" >Length of Data : Variable 1 to 7
<p>
                           01 when no data
<p>
                           07 maximum
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Charge Information
   </td>
   <td colspan="2" >0 = No Charge Information
<p>
1 = 1 cent unit
<p>
2 = 0.1 cent unit
<p>
3 = 10 cent unit
<p>
4 = $1 unit
<p>
5 = $10 unit
<p>
6 = Calling Metering (4 digits)
<p>
F = Charge Information Error
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td colspan="3" >Charge Data (Basic Charge Unit x 10<sup>0</sup>)
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td colspan="3" >Charge Data (Basic Charge Unit x 10<sup>1</sup>)
   </td>
  </tr>
  <tr>
   <td>008
   </td>
   <td colspan="3" >Charge Data (Basic Charge Unit x 10<sup>2</sup>)
   </td>
  </tr>
  <tr>
   <td>009
   </td>
   <td colspan="3" >Charge Data (Basic Charge Unit x 10<sup>3</sup>)
   </td>
  </tr>
  <tr>
   <td>010
   </td>
   <td colspan="3" >Charge Data (Basic Charge Unit x 10<sup>4</sup>)
   </td>
  </tr>
  <tr>
   <td>011
   </td>
   <td colspan="3" >Charge Data (Basic Charge Unit x 10<sup>5</sup>)
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td colspan="2" >1
   </td>
   <td rowspan="2" >Kind of Data : 16 Calling Station ANI
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td colspan="2" >6
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td colspan="2" >
   </td>
   <td rowspan="2" >Length of Data : Variable 1 to 33
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td colspan="2" >
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td colspan="2" >ANI Present Identifier
   </td>
   <td>0 = Unable to output
<p>
1 = Display
<p>
2 = Unable to Notify
<p>
3 = Out of Service (Out of Area)
<p>
4 = Public Telephone Origination
   </td>
  </tr>
  <tr>
   <td>006~037
   </td>
   <td colspan="2" >Calling Party Number
   </td>
   <td>Max 32 digits
   </td>
  </tr>
</table>

**<span style="text-decoration:underline;">KL Record Cont:</span>**

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>1
   </td>
   <td rowspan="2" >Kind of Data : 17 Change Code
<p>
                       (May be omitted)
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>7
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>
   </td>
   <td rowspan="2" >Length of Data : Variable 1 to 32
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>005~036
   </td>
   <td>Change Code
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>ETX
   </td>
   <td>End of Text
   </td>
  </tr>
</table>

**2.8  <span style="text-decoration:underline;">KM Record – IMX Format – Station to Station</span>**

    Programming information for this format can be found in Section 1.4


    The IMX Format is structured in such a fashion as to compress the data stream, maximizing it’s efficiency by elimination of unnecessary gaps in data.  Instead of providing fixed byte sizes for the various fields, the new format provides indexes (i.e. Kind of Data) that will describe the data and length to follow.

#### Valid Data for Outgoing Calls

<table>
  <tr>
   <td><strong>Kind of Data</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td>01
   </td>
   <td>Outgoing Trunk / Incoming Trunk information
   </td>
  </tr>
  <tr>
   <td>02
   </td>
   <td>Calling Party Information (Physical Number)
   </td>
  </tr>
  <tr>
   <td>03
   </td>
   <td>Calling Party Information (Telephone Number)
   </td>
  </tr>
  <tr>
   <td>04
   </td>
   <td>Called Party Information (Physical Number)
   </td>
  </tr>
  <tr>
   <td>05
   </td>
   <td>Called Party Information (Telephone Number)
   </td>
  </tr>
  <tr>
   <td>06
   </td>
   <td>Call Start Time / Call End Time
   </td>
  </tr>
  <tr>
   <td>07
   </td>
   <td>Account Code
   </td>
  </tr>
  <tr>
   <td>08
   </td>
   <td>Condition B Information
   </td>
  </tr>
  <tr>
   <td>10
   </td>
   <td>Dial Code
   </td>
  </tr>
  <tr>
   <td>17
   </td>
   <td>Change Code
   </td>
  </tr>
</table>

#### Example

**<span style="text-decoration:underline;">KM Record Cont:</span>**

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>000
   </td>
   <td>STX
   </td>
   <td>Start of Text
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>0
   </td>
   <td>System Address; fixed data
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>!
   </td>
   <td>Unit Address
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>Entry Index “K”
   </td>
   <td>“K” = SMDR record
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>Type of Record “M”
   </td>
   <td>“M” = Incoming Call / IMX Format
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>0
   </td>
   <td rowspan="2" >Kind of Data : 02 Calling Party Information (Physical number)
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>2
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>1
   </td>
   <td rowspan="2" >Length of Data = 10 characters
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Calling Party Identification
   </td>
   <td>0 = PBX/CTX (DID) station
<p>
1 = Attendant Console
<p>
2 = Incoming Trunk
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>Tenant – 1<sup>st</sup> digit
   </td>
   <td rowspan="3" >Calling Party Tenant
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>Tenant – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>008
   </td>
   <td>Tenant – 3<sup>rd</sup> digit
   </td>
  </tr>
  <tr>
   <td>009
   </td>
   <td>Calling Number – 1
   </td>
   <td rowspan="6" >Information shown in Calling Number fields depends on the Calling Party Identification.  When character 011 is;
<p>
0 – Station number is shown
<p>
1 – Attendant number is shown
<p>
2 – 3 digit Route and Trunk number
   </td>
  </tr>
  <tr>
   <td>010
   </td>
   <td>Calling Number – 2
   </td>
  </tr>
  <tr>
   <td>011
   </td>
   <td>Calling Number – 3
   </td>
  </tr>
  <tr>
   <td>012
   </td>
   <td>Calling Number – 4
   </td>
  </tr>
  <tr>
   <td>013
   </td>
   <td>Calling Number – 5
   </td>
  </tr>
  <tr>
   <td>014
   </td>
   <td>Calling Number – 6
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>0
   </td>
   <td rowspan="2" >Kind of Data : 03 Calling Party Number (Telephone Number)
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>3
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>
   </td>
   <td rowspan="2" >Length of Data : Variable 3 to 22
<p>
                           03 when no data
<p>
                           22 maximum
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Fusion Point Code – 1
   </td>
   <td rowspan="3" >Fusion Point Code : If no Fusion Point Code present then these fields will be set to ‘0’
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>Fusion Point Code – 2
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>Fusion Point Code – 3
   </td>
  </tr>
  <tr>
   <td>008
   </td>
   <td>User Group – 1
   </td>
   <td rowspan="3" >Fusion User Group Number
   </td>
  </tr>
  <tr>
   <td>009
   </td>
   <td>User Group – 2
   </td>
  </tr>
  <tr>
   <td>010
   </td>
   <td>User Group – 3
   </td>
  </tr>
  <tr>
   <td>011~026
   </td>
   <td>Calling Party Number
   </td>
   <td>Calling Party Number (logical ; 16 digits)
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>0
   </td>
   <td rowspan="2" >Kind of Data : 04 Called Party Information (Physical number)
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>4
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>1
   </td>
   <td rowspan="2" >Length of Data = 10 characters
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Calling Party Identification
   </td>
   <td>0 = PBX/CTX (DID) station
<p>
1 = Attendant Console
<p>
2 = Incoming Trunk
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>Tenant – 1<sup>st</sup> digit
   </td>
   <td rowspan="3" >Called Party Tenant
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>Tenant – 2<sup>nd</sup> digit
   </td>
  </tr>
  <tr>
   <td>008
   </td>
   <td>Tenant – 3<sup>rd</sup> digit
   </td>
  </tr>
  <tr>
   <td>009
   </td>
   <td>Calling Number – 1
   </td>
   <td rowspan="6" >Information shown in Called Number fields depends on the Called Party Identification.  When character 011 is;
<p>
0 – Station number is shown
<p>
1 – Attendant number is shown
<p>
2 – 3 digit Route and Trunk number
   </td>
  </tr>
  <tr>
   <td>010
   </td>
   <td>Calling Number – 2
   </td>
  </tr>
  <tr>
   <td>011
   </td>
   <td>Calling Number – 3
   </td>
  </tr>
  <tr>
   <td>012
   </td>
   <td>Calling Number – 4
   </td>
  </tr>
  <tr>
   <td>013
   </td>
   <td>Calling Number – 5
   </td>
  </tr>
  <tr>
   <td>014
   </td>
   <td>Calling Number – 6
   </td>
  </tr>
</table>

<p style="text-align: right">
<strong><span style="text-decoration:underline;">KM Record Cont:</span></strong></p>

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>0
   </td>
   <td rowspan="2" >Kind of Data : 05 Called Party Number (Telephone Number)
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>5
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>
   </td>
   <td rowspan="2" >Length of Data : Variable 3 to 22
<p>
                           03 when no data
<p>
                           22 maximum
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Fusion Point Code – 1
   </td>
   <td rowspan="3" >Fusion Point Code : If no Fusion Point Code present then these fields will be set to ‘0’
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>Fusion Point Code – 2
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>Fusion Point Code – 3
   </td>
  </tr>
  <tr>
   <td>008
   </td>
   <td>User Group – 1
   </td>
   <td rowspan="3" >Fusion User Group Number
   </td>
  </tr>
  <tr>
   <td>009
   </td>
   <td>User Group – 2
   </td>
  </tr>
  <tr>
   <td>010
   </td>
   <td>User Group – 3
   </td>
  </tr>
  <tr>
   <td>011~026
   </td>
   <td>Calling Party Number
   </td>
   <td>Called Party Number (logical ; 16 digits)
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>0
   </td>
   <td rowspan="2" >Kind of Data : 06 Call Start / End Time
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>6
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>3
   </td>
   <td rowspan="2" >Length of Data : 34 characters
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>4
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Year – Thousandths
   </td>
   <td rowspan="4" >Call Start : Year
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>Year – Hundredths
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>Year – Tenths
   </td>
  </tr>
  <tr>
   <td>008
   </td>
   <td>Year – Ones
   </td>
  </tr>
  <tr>
   <td>009
   </td>
   <td>Month – Tenths
   </td>
   <td rowspan="2" >Call Start : Month
   </td>
  </tr>
  <tr>
   <td>010
   </td>
   <td>Month – Ones
   </td>
  </tr>
  <tr>
   <td>011
   </td>
   <td>Day – Tenths
   </td>
   <td rowspan="2" >Call Start : Day
   </td>
  </tr>
  <tr>
   <td>012
   </td>
   <td>Day – Ones
   </td>
  </tr>
  <tr>
   <td>013
   </td>
   <td>Hour – Tenths
   </td>
   <td rowspan="2" >Call Start : Hour
   </td>
  </tr>
  <tr>
   <td>014
   </td>
   <td>Hour – Ones
   </td>
  </tr>
  <tr>
   <td>015
   </td>
   <td>Minute – Tenths
   </td>
   <td rowspan="2" >Call Start : Minute
   </td>
  </tr>
  <tr>
   <td>016
   </td>
   <td>Minute – Ones
   </td>
  </tr>
  <tr>
   <td>017
   </td>
   <td>Second – Tenths
   </td>
   <td rowspan="2" >Call Start : Second
   </td>
  </tr>
  <tr>
   <td>018
   </td>
   <td>Second – Ones
   </td>
  </tr>
  <tr>
   <td>019
   </td>
   <td>Milli-Second – Hundredths
   </td>
   <td rowspan="3" >Call Start : Milli-Second
   </td>
  </tr>
  <tr>
   <td>020
   </td>
   <td>Milli-Second – Tenths
   </td>
  </tr>
  <tr>
   <td>021
   </td>
   <td>Milli-Second – Ones
   </td>
  </tr>
  <tr>
   <td>022
   </td>
   <td>Year – Thousandths
   </td>
   <td rowspan="4" >Call End : Year
   </td>
  </tr>
  <tr>
   <td>023
   </td>
   <td>Year – Hundredths
   </td>
  </tr>
  <tr>
   <td>024
   </td>
   <td>Year – Tenths
   </td>
  </tr>
  <tr>
   <td>025
   </td>
   <td>Year – Ones
   </td>
  </tr>
  <tr>
   <td>026
   </td>
   <td>Month – Tenths
   </td>
   <td rowspan="2" >Call End : Month
   </td>
  </tr>
  <tr>
   <td>027
   </td>
   <td>Month – Ones
   </td>
  </tr>
  <tr>
   <td>028
   </td>
   <td>Day – Tenths
   </td>
   <td rowspan="2" >Call End : Day
   </td>
  </tr>
  <tr>
   <td>029
   </td>
   <td>Day – Ones
   </td>
  </tr>
  <tr>
   <td>030
   </td>
   <td>Hour – Tenths
   </td>
   <td rowspan="2" >Call End : Hour
   </td>
  </tr>
  <tr>
   <td>031
   </td>
   <td>Hour – Ones
   </td>
  </tr>
  <tr>
   <td>032
   </td>
   <td>Minute – Tenths
   </td>
   <td rowspan="2" >Call End : Minute
   </td>
  </tr>
  <tr>
   <td>033
   </td>
   <td>Minute – Ones
   </td>
  </tr>
  <tr>
   <td>034
   </td>
   <td>Second – Tenths
   </td>
   <td rowspan="2" >Call End : Second
   </td>
  </tr>
  <tr>
   <td>035
   </td>
   <td>Second – Ones
   </td>
  </tr>
  <tr>
   <td>036
   </td>
   <td>Milli-Second – Hundredths
   </td>
   <td rowspan="3" >Call End : Milli-Second
   </td>
  </tr>
  <tr>
   <td>037
   </td>
   <td>Milli-Second – Tenths
   </td>
  </tr>
  <tr>
   <td>038
   </td>
   <td>Milli-Second – Ones
   </td>
  </tr>
</table>

**<span style="text-decoration:underline;">KM Record Cont:</span>**

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>0
   </td>
   <td rowspan="2" >Kind of Data : 07 Account Code
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>7
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>
   </td>
   <td rowspan="2" >Length of Data : Variable 1 to 16
<p>
                           01 when no data
<p>
                          16 maximum
<p>
(<em>ASYDL Index 805 can increase the maximum to 24</em>)
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>005~020
   </td>
   <td>Account Code
   </td>
   <td>Account Code max 16 digits
<p>
(<em>ASYDL Index 805 can increase the maximum to 24</em>)
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>0
   </td>
   <td rowspan="2" >Kind of Data : 08 Condition Codes
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>8
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>0
   </td>
   <td rowspan="2" >Length of Data : 3 characters
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>3
   </td>
  </tr>
  <tr>
   <td>005
   </td>
   <td>Condition Code Zero (C0)
   </td>
   <td>0 = <em>No Condition</em>
<p>
1 = Call was transferred
<p>
2 = Billing is continued
<p>
3 = Call was transferred & Billing is
<p>
      continued
<p>
4 = Call was transferred to last called
<p>
      party
   </td>
  </tr>
  <tr>
   <td>006
   </td>
   <td>Condition Code One (C1)
   </td>
   <td>Call Origination is:
<p>
0 = <em>No Condition</em>
<p>
1 = by OG Queuing
<p>
2 = by dialing with Account Code
<p>
3 = by OG Queuing & dialing with Account
<p>
      Code
<p>
4 = by Forward Outside
<p>
5 = <em>Not Used</em>
<p>
6 = by Forward Outside & dialing with
<p>
      Account Code
   </td>
  </tr>
  <tr>
   <td>007
   </td>
   <td>Condition Code Two (C2)
   </td>
   <td>Call Origination is:
<p>
0 = Direct
<p>
1 = via Att Con
<p>
2 = Direct (Alternate Routing)
<p>
3 = via Att Con (Alternate Routing)
<p>
4 = Direct (LCR Routing)
<p>
5 = via Att Con (LCR Routing)
<p>
6 = Direct (Called number = first 6 digits of
<p>
      change code)
<p>
7 = via Att Con (Called number = first 6
<p>
      digits of change code)
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>1
   </td>
   <td rowspan="2" >Kind of data : 10 Dialed Number
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>
   </td>
   <td rowspan="2" >Length of Data : Variable 1 to 32
<p>
                           01 when no data
<p>
                           32 maximum
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>005~037
   </td>
   <td>Number Dialed (sent?)
   </td>
   <td>
   </td>
  </tr>
</table>

**<span style="text-decoration:underline;">KM Record Cont:</span>**

<table>
  <tr>
   <td><strong>Character</strong>
   </td>
   <td><strong>Name & Description</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>1
   </td>
   <td rowspan="2" >Kind of Data : 17 Change Code
<p>
                       (May be omitted)
   </td>
  </tr>
  <tr>
   <td>002
   </td>
   <td>7
   </td>
  </tr>
  <tr>
   <td>003
   </td>
   <td>
   </td>
   <td rowspan="2" >Length of Data : Variable 1 to 32
   </td>
  </tr>
  <tr>
   <td>004
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>005~036
   </td>
   <td>Change Code
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>001
   </td>
   <td>ETX
   </td>
   <td>End of Text
   </td>
  </tr>
</table>

# This page is left blank for your notes SECTION

# 3

## SMDR - TCP/IP DESCRIPTION

    The 2400IPX Series PBX is capable of transmitting SMDR records across a TCP/IP network.  This section will give a basic explanation of TCP/IP data format as it applies to transmitting SMDR records.  Also a description of data specific to NEC SMDR transmission across TCP/IP will be explained.


    This is not intended to be a detailed explanation of how TCP/IP or Ethernet works.  It is understood that the reader has a basic understanding of TCP/IP and Ethernet.

* See Section 1.3 for programming assignments.

    Before an SMDR record can be transmitted onto a data network, it must be encapsulated with various headers.  The receiving equipment will strip off the headers before translating the data.  

<p id="gdcalert8" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image8.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert9">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image8.jpg "image_tooltip")

            **SMDR Identifier : **The SMDR Identifier contains information that the PBX and the Billing Equipment use to communicate.  


            **TCP Header :  **The TCP Header contains the Port number that the sending and receiving IP applications will use to connect.


            **IP Header : ** The IP Header contains the IP Address of the sending and receiving network interface cards.


            **Ethernet Header :  **The Ethernet Header contains the MAC Address (hardware address) of the sending and receiving network interface cards.

**3.0  <span style="text-decoration:underline;">Message Sequence</span>**

    When the Billing Equipment comes online, it will associate a socket (port and IP address) and send a Connection Request to the PBX.  The PBX will only associate a socket upon receipt of a Connection Request.  The PBX will then send a Connection Accepted back to the Billing Equipment and SMDR Identifiers will be sent and responded to at regular intervals.  


    **SMDR Sending Sequence**


    When SMDR is to be sent via TCP/IP, the PBX will not automatically send the records to the billing equipment (e.g. AimWorx).  The billing equipment must send a request to the PBX for the SMDR records, called a Data Request Identifier.  The PBX will buffer SMDR records until a Data Request is received.  Once a Data Request is received the PBX will send the SMDR records to the billing equipment using a Data Send Identifier.  The billing equipment will then send an acknowledgment indicating that it correctly received the SMDR records by sending a Client Response Identifier.

<p id="gdcalert9" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image9.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert10">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image9.jpg "image_tooltip")

    The Sending Data Identifier and Client Response Identifier use a sequence number to determine which Client Response is acknowledging which Sending Data.  For example; a Sending Data with a sequence set as 1 will be acknowledged with a Client Response with a sequence set as 1.  The sequence number will range from 0 to 9.


    The billing equipment will send a Data Request Identifier about every five seconds, however this timer can be set from 1 to 30 seconds.  If the PBX receives a Data Request but does not have any SMDR records in it's buffer to be sent, it will respond with a Server Response Identifier.

<p id="gdcalert10" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image10.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert11">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image10.jpg "image_tooltip")

            **Status Monitoring Sequence**


    If the billing equipment is not requesting SMDR records but needs to ensure the communication path through the network is up, the billing equipment will send a Status Monitoring Identifier.  The PBX will respond with a Server Response Identifier.  These Identifiers act as heartbeat or keep alive messages.

<p id="gdcalert11" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image11.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert12">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image11.jpg "image_tooltip")

    **Error Sequence : Duplicate SMDR Records**


    If the PBX does not receive Client Response, receives a Client Response NACK, or receives a Client Response with an incorrect sequence number, it will retransmit the previously sent SMDR record upon receiving the next Data Request.

<p id="gdcalert12" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image12.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert13">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image12.jpg "image_tooltip")

    The billing equipment will compare the SMDR records received in succession to check whether the SMDR records are identical.  Duplicate records are discarded and a Client Response ACK is sent to the PBX, which tells the PBX to stop sending the duplicate records.


    


    **Error Sequence : PBX Send Data Error**


    If in response to a Data Request Identifier the PBX sends a Sending Data Identifier but the billing equipment does not receive it, then the billing equipment will re-send a Data Request.  If the PBX receives a set number of Data Requests without receiving a Client Response ACK, the PBX will output an alarm.

<p id="gdcalert13" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image13.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert14">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image13.jpg "image_tooltip")

    **Error Sequence : Billing Equipment Error**


    Once the billing equipment has connected to the PBX, the PBX will expect to see either a Status Monitoring Identifier or Data Request Identifier being sent at regular intervals.  If the PBX does not receive one of the messages within a preset time, it will output an alarm and discard the associated socket.

<p id="gdcalert14" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image14.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert15">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image14.jpg "image_tooltip")

    **Error Sequence : PBX Error**


    If the PBX fails to respond to a predetermined number of consecutively sent Status Monitor Identifiers, the billing equipment will discard it's associated socket and begin the connection sequence again.

<p id="gdcalert15" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image15.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert16">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image15.jpg "image_tooltip")

    The billing equipment will make six attempts by default before discarding the socket.  The number of attempts can range from 1 to 15.  A Status Monitoring Identifier will be sent about every ten seconds.


    **Parity Error **

Each SMDR Identifier ends with a Parity Byte.  When a parity error occurs a predetermined number of times consecutively (default setting is six times), the billing equipment will output an alarm, discard the associated socket and begin the connection sequence again.  If the parity error occurs at the PBX side, the billing equipment will retransmit the last SMDR Identifier it sent.**3.1  <span style="text-decoration:underline;">Ethernet - TCP/IP Packet Description</span>**

    In the NEAX 2400 PBX, SMDR Identifiers are transmitted on an Ethernet LAN using TCP/IP Packets.   The TCP/IP Packet will be encapsulated into an Ethernet Frame to be sent on the customers LAN.  The Ethernet Frame that SMDR uses is made up of four parts;

* Ethernet Header : Contains the MAC Address
* IP Header : Contains the IP Address
* TCP Header : Contains the Port Address
* Data : Contains the SMDR Identifiers and SMDR Records

<p id="gdcalert16" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image16.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert17">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image16.jpg "image_tooltip")

    The following pages show the structure of the Ethernet, IP, and TCP Headers.  Only a basic description is given as a detailed explanation of the functionality of each byte is beyond the scope of this document.  **<span style="text-decoration:underline;">Ethernet Header Structure</span>**

<p id="gdcalert17" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image17.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert18">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image17.jpg "image_tooltip")

```
    00 10 A4 E1 94 FF 00 00 4C A4 72 1C 08 00 45 00 01 1C 00 4C 00 00 40 06
    CC BB 0A C8 4B E1 0A C8 4B 64 EA 6A 04 20 00 0E 39 76 00 55 37 62 50 18
    22 38 3D 95 00 00 16 32 30 30 31 32 36 30 30 31 02 30 21 4B 4B 30 31 31
    32 30 30 30 30 31 30 30 30 34 30 30 30 30 32 31 30 32 30 30 31 30 32 30
    30 30 39 30 33 30 33 30 30 30 30 36 33 34 32 30 30 32 30 34 30 38 31 30
    31 38 30 37 38 36 37 32 30 30 32 30 34 30 38 31 30 31 38 32 30 38 39 32
    30 38 30 33 30 30 34 30 39 31 38 30 30 30 30 31 30 30 30 30 30 30 30 30
    31 30 30 30 30 31 30 30 34 31 30 30 30 31 33 30 31 30 03 FE 
```

**Sample Ethernet frame with SMDR data highlighting the Ethernet Header**

    The Ethernet Header will show the origination and destination MAC (Media Access Control) addresses.  This will be the hardware address of the NIC (Network Interface Card) in the PBX and in the billing equipment (e.g. AimWorx).  This header will only be present in an Ethernet network (e.g. in a token ring network you won't have an Ethernet header).

<table>
  <tr>
   <td><strong>Byte</strong>
   </td>
   <td><strong>HEX Data</strong>
   </td>
   <td><strong>Definition</strong>
   </td>
  </tr>
  <tr>
   <td>1
   </td>
   <td><strong>00</strong>
   </td>
   <td rowspan="6" >Destination MAC address : 0010A4-E194FF
   </td>
  </tr>
  <tr>
   <td>2
   </td>
   <td><strong>10</strong>
   </td>
  </tr>
  <tr>
   <td>3
   </td>
   <td><strong>A4</strong>
   </td>
  </tr>
  <tr>
   <td>4
   </td>
   <td><strong>E1</strong>
   </td>
  </tr>
  <tr>
   <td>5
   </td>
   <td><strong>94</strong>
   </td>
  </tr>
  <tr>
   <td>6
   </td>
   <td><strong>FF</strong>
   </td>
  </tr>
  <tr>
   <td>7
   </td>
   <td><strong>00</strong>
   </td>
   <td rowspan="6" >Origination MAC address : 00004C-A4721C
   </td>
  </tr>
  <tr>
   <td>8
   </td>
   <td><strong>00</strong>
   </td>
  </tr>
  <tr>
   <td>9
   </td>
   <td><strong>4C</strong>
   </td>
  </tr>
  <tr>
   <td>10
   </td>
   <td><strong>A4</strong>
   </td>
  </tr>
  <tr>
   <td>11
   </td>
   <td><strong>72</strong>
   </td>
  </tr>
  <tr>
   <td>12
   </td>
   <td><strong>1C</strong>
   </td>
  </tr>
  <tr>
   <td>13
   </td>
   <td><strong>08</strong>
   </td>
   <td rowspan="2" >0800 = EtherType : Xerox Department of Defense Internet Protocol
<p>
(Normal Ethernet)
   </td>
  </tr>
  <tr>
   <td>14
   </td>
   <td><strong>00</strong>
   </td>
  </tr>
</table>

**<span style="text-decoration:underline;">IP Header Structure</span>**

<p id="gdcalert18" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image18.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert19">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image18.jpg "image_tooltip")

```
    00 10 A4 E1 94 FF 00 00 4C A4 72 1C 08 00 45 00 01 1C 00 4C 00 00 40 06
    CC BB 0A C8 4B E1 0A C8 4B 64 EA 6A 04 20 00 0E 39 76 00 55 37 62 50 18
    22 38 3D 95 00 00 16 32 30 30 31 32 36 30 30 31 02 30 21 4B 4B 30 31 31
    32 30 30 30 30 31 30 30 30 34 30 30 30 30 32 31 30 32 30 30 31 30 32 30
    30 30 39 30 33 30 33 30 30 30 30 36 33 34 32 30 30 32 30 34 30 38 31 30
    31 38 30 37 38 36 37 32 30 30 32 30 34 30 38 31 30 31 38 32 30 38 39 32
    30 38 30 33 30 30 34 30 39 31 38 30 30 30 30 31 30 30 30 30 30 30 30 30
    31 30 30 30 30 31 30 30 34 31 30 30 30 31 33 30 31 30 03 FE 
```

**Sample Ethernet frame with SMDR data highlighting the IP Header**

    The IP Header will show the origination and destination IP (Internet Protocol) addresses.  This header also will have Quality of Service information that is used to prioritize packet transmission on a network.

<table>
  <tr>
   <td><strong>Byte</strong>
   </td>
   <td><strong>HEX Data</strong>
   </td>
   <td><strong>Definition</strong>
   </td>
  </tr>
  <tr>
   <td>1
   </td>
   <td><strong>45</strong>
   </td>
   <td>IP Version 4 (Normal) / Length of IP Header = 20 bytes
   </td>
  </tr>
  <tr>
   <td>2
   </td>
   <td><strong>00</strong>
   </td>
   <td>TOS (Type Of Service) Byte : (Quality Of Service settings are here)
   </td>
  </tr>
  <tr>
   <td>3
   </td>
   <td><strong>01</strong>
   </td>
   <td rowspan="2" >Total Length of the IP Packet in bytes (Does not include the Ethernet Header)
   </td>
  </tr>
  <tr>
   <td>4
   </td>
   <td><strong>1C</strong>
   </td>
  </tr>
  <tr>
   <td>5
   </td>
   <td><strong>00</strong>
   </td>
   <td rowspan="2" >Identification : This is used in assembling fragments of a packet
   </td>
  </tr>
  <tr>
   <td>6
   </td>
   <td><strong>4C</strong>
   </td>
  </tr>
  <tr>
   <td>7
   </td>
   <td><strong>00</strong>
   </td>
   <td rowspan="2" >Fragmentation Flags : Used to indicate if a packet is broken into fragments
<p>
Fragment Offset : This indicates the position of this fragment in the original packet.
   </td>
  </tr>
  <tr>
   <td>8
   </td>
   <td><strong>00</strong>
   </td>
  </tr>
  <tr>
   <td>9
   </td>
   <td><strong>40</strong>
   </td>
   <td>Time to Live = 64seconds / hops
   </td>
  </tr>
  <tr>
   <td>10
   </td>
   <td><strong>06</strong>
   </td>
   <td>Protocol of next header : 6 = TCP
   </td>
  </tr>
  <tr>
   <td>11
   </td>
   <td><strong>CC</strong>
   </td>
   <td rowspan="2" >Header Checksum : Used to determine if the data is corrupt
   </td>
  </tr>
  <tr>
   <td>12
   </td>
   <td><strong>BB</strong>
   </td>
  </tr>
  <tr>
   <td>13
   </td>
   <td><strong>0A</strong>
   </td>
   <td rowspan="4" >Origination IP Address : 0A.C8.4B.E1 (10.200.75.225)
   </td>
  </tr>
  <tr>
   <td>14
   </td>
   <td><strong>C8</strong>
   </td>
  </tr>
  <tr>
   <td>15
   </td>
   <td><strong>4B</strong>
   </td>
  </tr>
  <tr>
   <td>16
   </td>
   <td><strong>E1</strong>
   </td>
  </tr>
  <tr>
   <td>17
   </td>
   <td><strong>0A</strong>
   </td>
   <td rowspan="4" >Destination IP Address : 0A.C8.4B.64 (10.200.75.100)
   </td>
  </tr>
  <tr>
   <td>18
   </td>
   <td><strong>C8</strong>
   </td>
  </tr>
  <tr>
   <td>19
   </td>
   <td><strong>4B</strong>
   </td>
  </tr>
  <tr>
   <td>20
   </td>
   <td><strong>64</strong>
   </td>
  </tr>
</table>

            _Fragmentation:  If the data to be transmitted on the Network is too large to fit in a single TCP/IP Packet, the data will be broken into chunks (fragmented) and sent in separate Packets._

**<span style="text-decoration:underline;">TCP Header Structure</span>**

<p id="gdcalert19" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image19.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert20">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image19.jpg "image_tooltip")

```
    00 10 A4 E1 94 FF 00 00 4C A4 72 1C 08 00 45 00 01 1C 00 4C 00 00 40 06
    CC BB 0A C8 4B E1 0A C8 4B 64 EA 6A 04 20 00 0E 39 76 00 55 37 62 50 18
    22 38 3D 95 00 00 16 32 30 30 31 32 36 30 30 31 02 30 21 4B 4B 30 31 31
    32 30 30 30 30 31 30 30 30 34 30 30 30 30 32 31 30 32 30 30 31 30 32 30
    30 30 39 30 33 30 33 30 30 30 30 36 33 34 32 30 30 32 30 34 30 38 31 30
    31 38 30 37 38 36 37 32 30 30 32 30 34 30 38 31 30 31 38 32 30 38 39 32
    30 38 30 33 30 30 34 30 39 31 38 30 30 30 30 31 30 30 30 30 30 30 30 30
    31 30 30 30 30 31 30 30 34 31 30 30 30 31 33 30 31 30 03 FE 
```

**Sample Ethernet frame with SMDR data highlighting the TCP Header**

    The TCP Header will show the origination and destination Port addresses used by the applications in the PBX and Billing Equipment.

<table>
  <tr>
   <td><strong>Byte</strong>
   </td>
   <td><strong>HEX Data</strong>
   </td>
   <td><strong>Definition</strong>
   </td>
  </tr>
  <tr>
   <td>1
   </td>
   <td><strong>EA</strong>
   </td>
   <td rowspan="2" >Source Port = 60010 (this is the port used by the sending SMDR application.  Port 60010 is used by the PBX, 1056 is used by AimWorx)
   </td>
  </tr>
  <tr>
   <td>2
   </td>
   <td><strong>6A</strong>
   </td>
  </tr>
  <tr>
   <td>3
   </td>
   <td><strong>04</strong>
   </td>
   <td rowspan="2" >Destination Port = 1056 (this is the port used by the receiving SMDR application.  Port 60010 is used by the PBX, 1056 is used by AimWorx)
   </td>
  </tr>
  <tr>
   <td>4
   </td>
   <td><strong>20</strong>
   </td>
  </tr>
  <tr>
   <td>5
   </td>
   <td><strong>00</strong>
   </td>
   <td rowspan="4" >Sequence Number : Used to identify the position of the first byte in the data stream.
   </td>
  </tr>
  <tr>
   <td>6
   </td>
   <td><strong>0E</strong>
   </td>
  </tr>
  <tr>
   <td>7
   </td>
   <td><strong>39</strong>
   </td>
  </tr>
  <tr>
   <td>8
   </td>
   <td><strong>76</strong>
   </td>
  </tr>
  <tr>
   <td>9
   </td>
   <td><strong>00</strong>
   </td>
   <td rowspan="4" >Acknowledgment Number : This field contains the value of the next Sequence Number the sending equipment expects to see.
   </td>
  </tr>
  <tr>
   <td>10
   </td>
   <td><strong>55</strong>
   </td>
  </tr>
  <tr>
   <td>11
   </td>
   <td><strong>37</strong>
   </td>
  </tr>
  <tr>
   <td>12
   </td>
   <td><strong>62</strong>
   </td>
  </tr>
  <tr>
   <td>13
   </td>
   <td><strong>50</strong>
   </td>
   <td>Length of TCP Header (5) = 20 bytes
   </td>
  </tr>
  <tr>
   <td>14
   </td>
   <td><strong>18</strong>
   </td>
   <td>Flag Bits : 0001 1000 = NA/NA/URG/ACK   PSH/RST/SYN/FIN (<em>Note</em>)
   </td>
  </tr>
  <tr>
   <td>15
   </td>
   <td><strong>22</strong>
   </td>
   <td rowspan="2" >Window : Used to limit the amount of data sent in a packet.
   </td>
  </tr>
  <tr>
   <td>16
   </td>
   <td><strong>38</strong>
   </td>
  </tr>
  <tr>
   <td>17
   </td>
   <td><strong>3D</strong>
   </td>
   <td rowspan="2" >Checksum : Used to determine if the data received is corrupt
   </td>
  </tr>
  <tr>
   <td>18
   </td>
   <td><strong>95</strong>
   </td>
  </tr>
  <tr>
   <td>19
   </td>
   <td><strong>00</strong>
   </td>
   <td rowspan="2" >Urgent Pointer : Valid when the URG flag is set.  Used to tell the receiving application that this data should be processed before all others.
   </td>
  </tr>
  <tr>
   <td>20
   </td>
   <td><strong>00</strong>
   </td>
  </tr>
</table>

                    _Note: URG (Urgent Pointer Field) - Used to let the receiving application that urgency is required._


                    _ ACK (Acknowledgment) - Shows that the acknowledgment field is valid._


            _ PSH (Push) - Used to tell the receiving side to send all of its data to the receiving application._


            _ RST (Reset) - Used to request a connection reset._


                    _ SYN (Synchronization) - Used to synchronize the sequence numbers when initiating a connection._


                    _ FIN (Finish) - Indicates the sending application has finished sending the data stream._

**<span style="text-decoration:underline;">Data / SMDR Identifier</span>**

<p id="gdcalert20" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image20.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert21">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image20.jpg "image_tooltip")

```
    00 10 A4 E1 94 FF 00 00 4C A4 72 1C 08 00 45 00 01 1C 00 4C 00 00 40 06
    CC BB 0A C8 4B E1 0A C8 4B 64 EA 6A 04 20 00 0E 39 76 00 55 37 62 50 18
    22 38 3D 95 00 00 16 32 30 30 31 32 36 30 30 31 02 30 21 4B 4B 30 31 31
    32 30 30 30 30 31 30 30 30 34 30 30 30 30 32 31 30 32 30 30 31 30 32 30
    30 30 39 30 33 30 33 30 30 30 30 36 33 34 32 30 30 32 30 34 30 38 31 30
    31 38 30 37 38 36 37 32 30 30 32 30 34 30 38 31 30 31 38 32 30 38 39 32
    30 38 30 33 30 30 34 30 39 31 38 30 30 30 30 31 30 30 30 30 30 30 30 30
    31 30 30 30 30 31 30 30 34 31 30 30 30 31 33 30 31 30 03 FE 
```

**Sample Ethernet frame highlighting the SMDR Identifier and SMDR Record**

    The Data portion of the frame contains the SMDR Identifier and SMDR Records.  


    The SMDR Records will only be present if proceeded by a "Sending Data" SMDR Identifier.  Other SMDR Identifiers may be present for other purposes as outlined below.

**3.2  <span style="text-decoration:underline;">SMDR Identifier General Information</span>**

    SMDR Identifiers are NEC Proprietary messages used for communication between the PBX and the SMDR collection equipment (e.g. AimWorx). 

<table>
  <tr>
   <td><strong>SMDR Header</strong>
   </td>
   <td><strong>Direction</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td>Data Request
<p>
(Identifier : 1)
   </td>
   <td>Client 🡪 Server
   </td>
   <td>Sent by the client when it requests the server to send billing data.
   </td>
  </tr>
  <tr>
   <td>Sending Data
<p>
(Identifier : 2)
   </td>
   <td>Server 🡪 Client
   </td>
   <td>Response to a Data Request.  This includes the billing data (SMDR Records).
   </td>
  </tr>
  <tr>
   <td>Client Response
<p>
(Identifier : 4)
   </td>
   <td>Client 🡪 Server
   </td>
   <td>Response to a Sending Data.  This is an ACK from the client to indicate it received the billing data.
   </td>
  </tr>
  <tr>
   <td>Status Monitoring
<p>
(Identifier : 5)
   </td>
   <td>Client 🡪 Server
   </td>
   <td>Used in monitoring the server status from the client's viewpoint or the client from the server's viewpoint.  At the same time, this is used to notify the server of the client status.
<p>
This is the Heartbeat or Keep Alive message.
   </td>
  </tr>
  <tr>
   <td>Server Response
<p>
(Identifier : 3)
   </td>
   <td>Server 🡪 Client
   </td>
   <td>Response to a Status Monitoring or a Data Request if there is no billing data to send.
   </td>
  </tr>
  <tr>
   <td>Connection Disconnect
<p>
(Identifier : 6)
   </td>
   <td>Client 🡪 Server
   </td>
   <td>Sent from the client to the server to disconnect the connection.
   </td>
  </tr>
</table>

**<span style="text-decoration:underline;">SMDR Identifier 1 : Data Request</span>**

<p id="gdcalert21" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image21.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert22">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image21.jpg "image_tooltip")

```
    00 00 4C A4 72 1C 00 10 A4 E1 94 FF 08 00 45 00 00 32 63 09 40 00 80 06 EA E7 0A C8 4B 64 0A C8 4B E1 04 20 EA 6A 00 55 37 6E 00 0E 3A 6A 50 18 21 44 A7 25 00 00 16 31 30 30 30 30 32 30 30 FC
```

**Sample Ethernet frame with Data Request Identifier**

    The SMDR equipment (e.g. AimWorx) sends the Data Request Identifier to the PBX when it is requesting that billing data is to be sent.


    When the SMDR equipment sends a Data Request to a PBX, the PBX will respond with either a Send Data, which includes the billing data, or a Server Response if there is no billing data to be sent.


    When a Data Request has been sent to a PBX, that PBX must respond within 10 seconds (default timer setting, timer value can be set from 1 to 30 seconds).  After 10 seconds, the SMDR equipment will send the Data Request again.  The Data Request will be re-sent a predetermined number of times (6?) and if there is still no response from the PBX, the socket will be discarded and the IP connection reset.

<p id="gdcalert22" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image22.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert23">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image22.jpg "image_tooltip")

    **Synchronization Character **: Data is fixed at '16'.  Used to maintain synchronization.


    **Identifier Kind** : Tells what type of SMDR Identifier is being sent.


    **Length** : How many characters of data are to follow in the SMDR Identifier.


            **Device Number** : Tells which SMDR Device is sending this data.  There can be a total of four SMDR Devices configured using ASYDL Indexes 578, 579, 580, and 581.


    **Parity Byte** : Used for error detection.**<span style="text-decoration:underline;">SMDR Identifier 2 : Sending Data</span>**

<p id="gdcalert23" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image23.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert24">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image23.jpg "image_tooltip")

```
    00 10 A4 E1 94 FF 00 00 4C A4 72 1C 08 00 45 00 01 1C 00 4C 00 00 40 06
    CC BB 0A C8 4B E1 0A C8 4B 64 EA 6A 04 20 00 0E 39 76 00 55 37 62 50 18
    22 38 3D 95 00 00 16 32 30 30 31 32 36 30 30 31 02 30 21 4B 4B 30 31 31
    32 30 30 30 30 31 30 30 30 34 30 30 30 30 32 31 30 32 30 30 31 30 32 30
    30 30 39 30 33 30 33 30 30 30 30 36 33 34 32 30 30 32 30 34 30 38 31 30
    31 38 30 37 38 36 37 32 30 30 32 30 34 30 38 31 30 31 38 32 30 38 39 32
    30 38 30 33 30 30 34 30 39 31 38 30 30 30 30 31 30 30 30 30 30 30 30 30
    31 30 30 30 30 31 30 30 34 31 30 30 30 31 33 30 31 30 03 FE 
```

**Sample Ethernet Frame with Sending Data Identifier**

    The PBX sends the Sending Data Identifier to the SMDR equipment after a Data Request header has been received.  One or more Call Records will be included in this Identifier.

<p id="gdcalert24" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image24.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert25">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image24.jpg "image_tooltip")

    **Synchronization Character **: Data is fixed at '16'.  Used to maintain synchronization.


    **Identifier Kind** : Tells what type of SMDR Identifier is being sent.


    **Length** : How many characters of data are to follow in the SMDR Identifier.


            **Device Number** : Tells which SMDR Device is sending this data.  There can be a total of four SMDR Devices configured using ASYDL Indexes 578, 579, 580, and 581.


            **Sequence Number** : Ranges from 0 to 9.  This is used to match acknowledgments to the correct sent messages.


    **Parity Byte** : Used for error detection.

**<span style="text-decoration:underline;">SMDR Identifier 3 : Server Response</span>**

<p id="gdcalert25" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image25.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert26">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image25.jpg "image_tooltip")

```
    00 10 A4 E1 94 FF 00 00 4C A4 72 1C 08 00 45 00 00 33 00 29 00 00 40 06 CD C7 0A C8 4B E1 0A C8 4B 64 EA 6A 04 1E 00 0C 33 72 00 53 31 72 50 18 22 38 E5 F1 00 00 16 33 30 30 30 30 33 30 30 32 CD 
```

**Sample Ethernet frame with Server Response Identifier**

    The PBX sends the Server Response Identifier to the SMDR equipment in response to a Data Request Identifier when there are no Call Records to send.  This header could also be sent in response to a Status Monitoring Identifier.

<p id="gdcalert26" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image26.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert27">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image26.jpg "image_tooltip")

    **Synchronization Character **: Data is fixed at '16'.  Used to maintain synchronization.


    **Identifier Kind** : Tells what type of SMDR Identifier is being sent.


    **Length** : How many characters of data are to follow in the SMDR Identifier.


            **Device Number** : Tells which SMDR Device is sending this data.  There can be a total of four SMDR Devices configured using ASYDL Indexes 578, 579, 580, and 581.


            **Response Number** : Indicates what type of response this message is;


                ** **1 -  Sent in response to a Data Request Identifier when no SMDR records are buffered.


                 2 - Send in response to a Status Monitoring Identifier.


    **Parity Byte** : Used for error detection.

**<span style="text-decoration:underline;">SMDR Identifier 4 : Client Response</span>**

<p id="gdcalert27" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image27.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert28">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image27.jpg "image_tooltip")

```
    00 00 4C A4 72 1C 00 10 A4 E1 94 FF 08 00 45 00 00 34 62 09 40 00 80 06 EB E5 0A C8 4B 64 0A C8 4B E1 04 20 EA 6A 00 55 37 62 00 0E 3A 6A 50 18 21 44 9F 2F 00 00 16 34 30 30 30 30 34 30 30 31 06 C8 
```

**Sample Ethernet frame with Client Response Identifier**

    The SMDR equipment sends the Client Response Identifier to the PBX in response to a Sending Data Identifier.  

<p id="gdcalert28" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image28.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert29">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image28.jpg "image_tooltip")

    **Synchronization Character **: Data is fixed at '16'.  Used to maintain synchronization.


    **Identifier Kind** : Tells what type of SMDR Identifier is being sent.


    **Length** : How many characters of data are to follow in the SMDR Identifier.


            **Device Number** : Tells which SMDR Device is sending this data.  There can be a total of four SMDR Devices configured using ASYDL Indexes 578, 579, 580, and 581.


            **Sequence Number** : Ranges from 0 to 9.  This is used to match acknowledgments to the correct sent messages.


            **ACK/NACK **: Acknowledgment / No Acknowledgment.  


            ** **6 - Acknowledgment


    **Parity Byte** : Used for error detection.

**<span style="text-decoration:underline;">SMDR Identifier 5 : Status Monitoring</span>**

<p id="gdcalert29" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image29.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert30">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image29.jpg "image_tooltip")

```
    00 00 4C A4 72 1C 00 10 A4 E1 94 FF 08 00 45 00 00 35 1A 09 40 00 80 06 33 E5 0A C8 4B 64 0A C8 4B E1 04 1E EA 6A 00 53 31 58 00 0C 33 67 50 18 22 38 88 0E 00 00 16 35 30 30 30 30 35 30 30 30 30 06 F9
```

**Sample Ethernet frame with Status Monitoring Identifier**

    The Status Monitoring Identifier is used to send PBX status to the SMDR equipment and/or SMDR equipment status to the PBX.

<p id="gdcalert30" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image30.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert31">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image30.jpg "image_tooltip")

    **Synchronization Character **: Data is fixed at '16'.  Used to maintain synchronization.


    **Identifier Kind** : Tells what type of SMDR Identifier is being sent.


    **Length** : How many characters of data are to follow in the SMDR Identifier.


            **Device Number** : Tells which SMDR Device is sending this data.  There can be a total of four SMDR Devices configured using ASYDL Indexes 578, 579, 580, and 581.


                **Client Device Information** : Tells which Client Device (billing equipment) is sending this message.


            **ACK/NACK **: Acknowledgment / No Acknowledgment.  


            ** **6 - Acknowledgment


    **Parity Byte** : Used for error detection.

**<span style="text-decoration:underline;">SMDR Identifier 6 : Connection Disconnect</span>**

<p id="gdcalert31" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image31.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert32">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image31.jpg "image_tooltip")

```
    00 00 4C A4 72 1C 00 10 A4 E1 94 FF 08 00 45 00 00 33 46 09 40 00 80 06 07 E7 0A C8 4B 64 0A C8 4B E1 04 1E EA 6A 00 53 32 76 00 0C 34 59 50 18 21 46 B6 21 00 00 16 36 30 30 30 30 33 30 30 06 FC
```

**Sample Ethernet frame with Connection Disconnect Identifier**

    The SMDR equipment sends the Connection Disconnect Identifier to the PBX to disconnect the connection.  In response to this Identifier, the PBX promptly performs processing to disconnect the connection.

<p id="gdcalert32" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image32.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert33">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image32.jpg "image_tooltip")

    **Synchronization Character **: Data is fixed at '16'.  Used to maintain synchronization.


    **Identifier Kind** : Tells what type of SMDR Identifier is being sent.


    **Length** : How many characters of data are to follow in the SMDR Identifier.


            **Device Number** : Tells which SMDR Device is sending this data.  There can be a total of four SMDR Devices configured using ASYDL Indexes 578, 579, 580, and 581.


            **ACK/NACK **: Acknowledgment / No Acknowledgment.  


            ** **6 - Acknowledgment


    **Parity Byte** : Used for error detection.

# SECTION

# 4

## CCIS CENTRALIZED BILLING MESSAGE DESCRIPTION

#

    This section does not fully cover CCIS Layer 3 messaging nor does it cover the use of CCIS trace utilities.  Only information needed to interpret the Centralized Billing Message will be covered.

#

    In a CCIS network, SMDR records that are created in all nodes can be sent to a central node to be output to the billing equipment.  The SMDR information is sent in a Centralized Billing Message (CBM) over the CCIS Signal Channel.  

**4.0  <span style="text-decoration:underline;">CCIS Message Format: 16-Z</span>**

#

    Once the CCIS trace has been initiated in a NEAX2400 PBX, it will print out the data in a 16-Z System Message.  A 16-Z message when printed will be divided into eight sections numbered 1 to 8.  Section 1 is the CCIS Header, which contains the same information for every CCIS message type; the originating & destination point codes, CIC used, and message type.  Specific to the CBM, the first part of section 2 gives sending information and includes; sending/receiving flag, ack/nack flag, resend flag, and sequence number.  The second part of section 2 will begin the SMDR information if applicable.

* The 16-Z format can only print a limited number of characters.  As a result, the last 36 characters of the SMDR data will not be printed.

 Header Sending Info SMDR Data

```
1:3F840180 0000002D 2:02000230 214B4130 3:31303030 33303031 4:31303031 20203039
5:31373136 35343134 6:30393137 31363534 7:31362020 20A00008 8:00000000 00000000
```

# SMDR Data

#

    Section 1: Header

#

    To decode the Header information you must first separate the data into Bytes (Octets), arrange the Bytes then convert the Bytes from hex to binary.

#

    Step 1

#

     Separate the Bytes and arrange them from 01 to 08.

#

<p id="gdcalert33" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image33.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert34">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image33.jpg "image_tooltip")

# Step 2

# Reverse the order of Bytes 03 thru 06

#

<p id="gdcalert34" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image34.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert35">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image34.jpg "image_tooltip")

# Step 3

# Convert Byte 01 from Hex to Decimal to find the total length of the message

#

<p id="gdcalert35" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image35.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert36">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image35.jpg "image_tooltip")

# Step 4

# Byte 02 is the Service Information Octet (SIO) and has a fixed value of 84 hex

#

<p id="gdcalert36" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image36.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert37">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image36.jpg "image_tooltip")

# Step 5a

#

     To find the Destination & Origination Point Codes and the Circuit Identification Code (CIC), first convert Bytes 07, 06, 05, 04, and 03 to binary.

#

<p id="gdcalert37" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image37.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert38">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image37.jpg "image_tooltip")

# Step 5b

#

     Divide the binary positions into to the three sections as shown.

#

<p id="gdcalert38" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image38.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert39">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image38.jpg "image_tooltip")

#

    Step 6

#

     To find the CIC number, convert the binary to decimal.

#

<p id="gdcalert39" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image39.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert40">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image39.jpg "image_tooltip")

# Step 7

# To find the Origination Point Code (OPC), convert the binary to decimal

#

<p id="gdcalert40" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image40.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert41">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image40.jpg "image_tooltip")

# Step 8

# To find the Destination Point Code (DPC), convert the binary to decimal

#

<p id="gdcalert41" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image41.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert42">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image41.jpg "image_tooltip")

# Step 9

#

     Byte 08 is the Heading Code, which tells what type of message is being sent.  This does not need to be converted to binary or decimal.  The hex value of 2D means the message is a Centralized Billing Message.  Other common Heading Codes are listed below.

#

<p id="gdcalert42" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image42.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert43">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image42.jpg "image_tooltip")

<table>
  <tr>
   <td>
<h1>Heading Code</h1>

   </td>
   <td>
<h1>Description</h1>

   </td>
  </tr>
  <tr>
   <td>
<h1>14</h1>

   </td>
   <td>
<h1>Address Complete Message (ACM) : Acknowledgement to IAI message</h1>

   </td>
  </tr>
  <tr>
   <td>
<h1>18</h1>

   </td>
   <td>
<h1>Release Guard Signal Message (RLG) : Acknowledgement to CLF message</h1>

   </td>
  </tr>
  <tr>
   <td>
<h1>21</h1>

   </td>
   <td>
<h1>Initial Address Message with Addition Information (IAI) : CCIS call setup</h1>

   </td>
  </tr>
  <tr>
   <td>
<h1>2D</h1>

   </td>
   <td>
<h1>Centralized Billing Message (CBM) : Transports SMDR records</h1>

   </td>
  </tr>
  <tr>
   <td>
<h1>2F</h1>

   </td>
   <td>
<h1>Answer Signal with Additional Info (AND) : CCIS call has connected</h1>

   </td>
  </tr>
  <tr>
   <td>
<h1>36</h1>

   </td>
   <td>
<h1>Clear Back Signal Message (CBK) : 1st party of a CCIS call disconnects</h1>

   </td>
  </tr>
  <tr>
   <td>
<h1>46</h1>

   </td>
   <td>
<h1>Clear Forward Signal Message (CLF) : 2nd party of a CCIS call disconnects</h1>

   </td>
  </tr>
</table>

#

    Section 2: Sending Information

#

    Sending Information is comprised of two bytes.  The first byte is Start Of Text and has a fixed value of 02 hex.  The second byte must be converted to binary and decoded as shown below.

#

<p id="gdcalert43" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image43.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert44">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image43.jpg "image_tooltip")

#

                Send/Receive : 0/1 -  Determines which side of the CCIS is sending the message.  "Send" is the PBX that is sending the SMDR, "Receive" is the PBX that is receiving the SMDR.

#

                Resend : 0/1 - This flag would be set to '1' in the event a CBM message from the Sending PBX must be resent.  This would happen on receiving a NACK from the Receiving PBX after sending a SMDR record.

#

                Sequence Number - The Sequence Number ranges from 0 to 3.  SMDR records are too large to be sent in a single CBM.  The first part of the SMDR record will be Sequence 0, and the ACK/NACK response will also be Sequence 0.  The second part of the SMDR record will be Sequence 1, and the ACK/NACK response will also be Sequence 1.

#

                ACK/NACK - Upon receiving a CBM with an SMDR record, the receiving PBX must send either an Acknowledge (ACK) response or No Acknowledge (NACK) response.  

```


#                  0 0 0 : ACK


#                  0 0 1 : NACK - Error detected


#                  0 1 0 : NACK - Wait


#                  0 1 1 : NACK - Delete


#                  1 0 0 : NACK - Clear
```

#

    Section 2 ~ 7: SMDR Record

#

    There are two formats that are used to put the raw SMDR data into a CBM message.  These formats are controlled by ASYD index 300, bit 0:

# Index 300, Bit 0 = 0 : Normal Format (does not include ANI from tandem ISDN route)

# Index 300, Bit 0 = 1 : Expanded Format (includes ANI from tandem ISDN route)

#

    Normal Format (ASYD Index 300 = 00)

#

    To read SMDR records within a CBM message when coded as normal format, each byte is one character (_refer to Appendix E_).

#

<p id="gdcalert44" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image44.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert45">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image44.jpg "image_tooltip")

#

    Expanded Format (ASYD Index 300 = 01)

#

    When ASYD Index 300 bit 0 is set to 1, the format that the SMDR data is placed in the CBM message is changed.  At the time of writing this chapter, a key for reading this format is unavailable.  

# Example CBM message from 2400 to 2400 in normal format

#

<p id="gdcalert45" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image45.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert46">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image45.jpg "image_tooltip")

```
SYSTEM MESSAGE  16-Z      CCIS/ISDN MESSAGE TRACE

1:3F840180 0000002D 2:02000230 214B4130 3:31303030 33303031 4:31303031 20203039
5:31373136 35343134 6:30393137 31363534 7:31362020 20A00008 8:00000000 00000000
```

<p id="gdcalert46" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image46.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert47">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image46.jpg "image_tooltip")

```
SYSTEM MESSAGE  16-Z      CCIS/ISDN MESSAGE TRACE

1:0C840240 0000002D 2:02800300 00000000 3:00000000 00000000 4:00000000 00000000
5:00000000 00000000 6:00000000 00000000 7:00000000 00A00000 8:00000000 00000000
```

<p id="gdcalert47" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image47.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert48">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image47.jpg "image_tooltip")

```
SYSTEM MESSAGE  16-Z      CCIS/ISDN MESSAGE TRACE

1:3F840180 0000002D 2:02082020 20202020 3:20202020 20202020 4:30303030 20202020
5:20202020 20202020 6:20202020 20203032 7:30323020 20A00008 8:00000000 00000000
```

<p id="gdcalert48" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image48.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert49">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image48.jpg "image_tooltip")

```
SYSTEM MESSAGE  16-Z      CCIS/ISDN MESSAGE TRACE

1:0C840240 0000002D 2:02880300 00000000 3:00000000 00000000 4:00000000 00000000
5:00000000 00000000 6:00000000 00000000 7:00000000 00A00000 8:00000000 00000000
```

# Example CBM message from 2400 to 2400 in expanded format

#

<p id="gdcalert49" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image49.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert50">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image49.jpg "image_tooltip")

```
SYSTEM MESSAGE  16-Z      CCIS/ISDN MESSAGE TRACE

1:3F840180 0000002D 2:02008491 0000008A 3:000A0084 0100A11A 4:00000000 00000000
5:00000000 00000000 6:00000000 00000000 7:00000000 00A00008 8:00000000 00000000
```

<p id="gdcalert50" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image50.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert51">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image50.jpg "image_tooltip")

```
SYSTEM MESSAGE  16-Z      CCIS/ISDN MESSAGE TRACE

1:0C840240 0000002D 2:02800300 00000000 3:00000000 00000000 4:00000000 00000000
5:00000000 00000000 6:00000000 00000000 7:00000000 00A00000 8:00000000 00000000
```

<p id="gdcalert51" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image51.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert52">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image51.jpg "image_tooltip")

```
SYSTEM MESSAGE  16-Z      CCIS/ISDN MESSAGE TRACE

1:3F840180 0000002D 2:02080000 00620262 3:02000000 00000002 4:20022000 00000000
5:00307982 47A11A00 6:00000000 00000000 7:00000000 00A00008 8:00000000 00000000
```

<p id="gdcalert52" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image52.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert53">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image52.jpg "image_tooltip")

```
SYSTEM MESSAGE  16-Z      CCIS/ISDN MESSAGE TRACE

1:0C840240 0000002D 2:02880300 00000000 3:00000000 00000000 4:00000000 00000000
5:00000000 00000000 6:00000000 00000000 7:00000000 00A00000 8:00000000 00000000
```

# Example CBM message from 2000 to 2400

#

<p id="gdcalert53" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image53.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert54">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image53.jpg "image_tooltip")

```
SYSTEM MESSAGE  16-Z      CCIS/ISDN MESSAGE TRACE

1:3F840240 0000002D 2:02000230 214B4130 3:31303130 31303031 4:35373338 20203039
5:32353135 31353132 6:30393235 31353135 7:31362020 20A00008 8:00000000 00000000
```

<p id="gdcalert54" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image54.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert55">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image54.jpg "image_tooltip")

```
SYSTEM MESSAGE  16-Z      CCIS/ISDN MESSAGE TRACE

1:0C840180 0000002D 2:02800300 00000000 3:00000000 00000000 4:00000000 00000000
5:00000000 00000000 6:00000000 00000000 7:00000000 00A00000 8:00000000 00000000
```

<p id="gdcalert55" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image55.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert56">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image55.jpg "image_tooltip")

```
SYSTEM MESSAGE  16-Z      CCIS/ISDN MESSAGE TRACE

1:3F840240 0000002D 2:02082020 20202020 3:20202020 20202020 4:30303030 20202020
5:20202020 20202020 6:20202020 20202020 7:20203020 20A00008 8:00000000 00000000
```

<p id="gdcalert56" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image56.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert57">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image56.jpg "image_tooltip")

```
SYSTEM MESSAGE  16-Z      CCIS/ISDN MESSAGE TRACE

1:0C840180 0000002D 2:02880300 00000000 3:00000000 00000000 4:00000000 00000000


# 5:00000000 00000000 6:00000000 00000000 7:00000000 00A00000 8:00000000 00000000
```

# This page is left blank for your notes<span style="text-decoration:underline;"> </span>SECTION

# 5

## SMDR Service Conditions and Limitations

**5.0  <span style="text-decoration:underline;">Service Conditions and Limitations</span>**

* Both incomplete and abandoned calls will be discarded by SMDR.  That is a call that disconnects before being answered or before answer supervision has taken place.
* If the outgoing call is directed to a trunk that cannot give answer supervision from the Central Office, the ‘start of call time’ is 18 seconds after the last digit dialed.  This timer can be manipulated (_see ASYD index’s 156 and 157 in Section 1.1_).
* During Station-to-Station Calling [S-11] when either of the two parties goes On-Hook, output of the billing information will be completed.
* On an incoming trunk call to the Attendant Console, the Attendant ‘call record’ will start upon answering and complete when the Attendant releases.  A station ‘call record’ will start when the Attendant releases and complete when the station goes on-hook.
* For Call Waiting-Termination [C-12], SMDR will begin recording the call when the call is answered, not when a Call Waiting Tone is heard.
* SMDR may be programmed to record all outgoing, all outgoing & incoming, or only toll calls (_see ARTD in Section 1.0_).
* The maximum number of digits dialed cannot exceed 24.
* If an Account Code [A-18] is dialed, the maximum number of digits of the dialed number is 22.
* Forced Account Code [F-7] can be recorded on SMDR for INWATS and CO incoming calls when used in conjunction with the Remote Access To System [R-2] service feature.  However, Forced Account Code cannot be registered on SMDR if the incoming Remote Access calls are terminated to stations via night service or DID [D-8].
* For Remote Access To System [R-2] tandem connections, the Forced Account Code [F-7] is registered for the outgoing trunks only.
* For Attendant-Controlled Conference [A-2]; if the Attendant adds a trunk to the conference, the Attendant conference line terminal is recorded.
* For Centralized Attendant Service (CAS) [C-20]; the SMDR record is provided for calls extended outward by a CAS Attendant.

**<span style="text-decoration:underline;">SMDR Service Conditions and Limitations Cont:</span>**

* For Serial Call [S-15], the duration of the total call is recorded on the last station call.
* Authorization Code [A-20] procedure 2 will be recorded in the SMDR, procedure 1 will not.
* When Station Hunting [S-7, 8, 9] takes place, the hunted-to station is recorded in called number field.
* The destination station is recorded on SMDR for the following features:

        Call Forwarding [C-2, 3, 5]


        Call Pickup [C-7, 30]

* For Call Forwarding-Intercept [C-25], when an incoming trunk call responds to Call Forwarding-Intercept to the Attendant Console; the SMDR will record the call as if it is a direct call to the Attendant Console.
* For Call Transfer-All Calls [C-11], either the first station, last station, or split billing is allowed with SMDR via ASYD index 33.  Split billing provides a separate call record for both before and after a call transfer.
* For Attendant Camp-On with Tone Indication [A-1], the called station number is recorded for the incoming C.O. calls via the Attendant Console (RRI2 of ARSC).  To record the time a destination station is on a call, split billing or last station billing is required (ASYD index 33).  With split billing, the time the Attendant Console is on the call is separated from the time the destination station is charged with the entire time of connection.
* For Least-Cost Routing-3/6-Digit [L-5], SMDR will record the digits sent rather than the digits dialed.
* When a line connection is established on the FCCS link, the billing data concerned is collected fully in the called station-side node, not in the calling station side.  The collected data is then transmitted to the SMDR terminal as the call finishes.

**5.1  <span style="text-decoration:underline;">SMDR Call Time Specifications:</span>**

* The base for Call Start Time and Call End Time is the time in the calling party-side node.
* In case there is a time difference between each node, related time difference data, based on the UCT (Universal Coordinated Time) standard, should be written in Network Data Memory (NDM) by using the ATDF command.
* Because billing information gathering is performed in the called party-side node, the Call Start Time in the originating node is determined in this way; the deduction of time between calling and called party nodes is added or subtracted to / from the called party-side time.  (If there is no time difference data in any [both] of the nodes, the Call Start Time is specified automatically by that in the called party-side node).
* A counter, not the clock providing the current time, is used for Call End Time calculation.  The calculation method is as follows:

1. Call Start Time (by using the clock) and the current counter value are registered to the Call Base Table, soon after a line connection is established.
2. Upon the call completion, the deduction between the counter value shown in (1.) and that renewed during the call exchange is calculated.
3. The deduction is transformed to a time (hour, minute, second, milli-second) format.
4. The transformed time is added to the Call Start Time registered in (1.).

* The counter-based time is renewed every 16.384 milli-seconds.

# This page is left blank for your notes<span style="text-decoration:underline;"> </span>SECTION

# 6

## SMDR Buffer Information for SP & AP

## 6.0  <span style="text-decoration:underline;">SMDR Buffer Description</span>

* 1 SMDR Call Record = 1 Block

    1 Block = 144 Bytes

* Maximum number of SMDR call records that can be stored are (numbers rounded down);

     28,000 IMG / Single-Processor Systems

     47,000 MMG/UMG

     47,000 * number of LMG’s IPX-UMG

    In an HDS MMG/UMG when a AP is used, the number of stored records can be reduced to 10,000 by a switch setting on the CP-50 in the AP:  SW1 – 5=OFF, 6=ON.

* If the SMDR Buffer overflows, subsequent calls are allowed to complete but are not recorded.  (_Note:  In Hotel/Motel systems calls can be restricted in an overflow condition by setting ASYD System Data 1, Index 67._)
* When Serial Output is used, there is a buffer on the I/O card that holds 80 records.  Be aware when testing that you may see 80 call records dump from the SP/AP buffer, but not see them dump out the I/O port.  Sometime later when the I/O card is reset, you may see 80 records dump out the I/O port but the SP/AP buffer shows no activity.
* SMDR call records are written into and read from the buffer sequentially.  The first eight bytes of each record will be the beginning address of the previous record and the beginning address of the next record, thus creating a ‘chain’ of records.  If the chain is broken, the program will go into B-Level loop.  Example;

 <span style="text-decoration:underline;">Normal</span> <span style="text-decoration:underline;">Broken</span>

 AB(data) AB(data)

 BC(data) CD(data)

 CD(data) DE(data)

 DE(data)

    **Data Structure of SMDR Buffer Areas**

      Previous memory address


      Next memory address

```
    00CFD084: 42 F4 CF CF 00 14 D1 CF 00 01 02 30 21 4B 45 31 B.........0!KE1
    00CFD094: 37 32 30 32 33 30 30 33 36 32 36 30 34 20 31 31   720230036260411
```

``Memory address (_Actual address will vary by software_)

    See Appendix E for converting the raw SMDR data to ASCII.


    The next and previous memory addresses must be inverted.  For example;  if the address shown in the buffer area is D1 CF 00 01, the actual address would be CF D1 01 00.**6.1  <span style="text-decoration:underline;">SMDR Buffer Header Information</span>**

**Head Addresses:**

****HDS UMG Rel. IV XE `00C10004` ICS ‘H’ Version `B7FFE0`

 HDS SIM Rel. V `D7FFE0` ICS ‘J’ Version `0DFFFE0`

 ICS ‘I’ Version `01FFFFE0`  IMX R8 ~ R11 `25FFFD0`

 **PBI**

 IMG/Single Processor:  00 MMG/UMG SP:  02/03 MMG/UMG AP:  04/05

# RDS / HDS / ICS Breakout

  M1HP M2HP M1EP M2EP

 00C10004: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 00C10014: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

  CBHP CBTP IDL LISC SCRN

    BLK

# IMX / IPX Breakout (expanded for fusion)

  M1HP M2HP M3HP M1EP

 25FFFD0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 25FFFE0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

   M2EP M3EP  CBHP CBTP

  IDL SCRN

  BLK LISC  FCBT

 25FFFF0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

**M1HP** : Head pointer for self PBX SMDR call record buffer.

**M1EP** : End pointer for self PBX SMDR call record buffer.

**M2HP** : Head pointer for SMDR call records received via CCIS from remote PBX’s.

**M2EP** : End pointer for SMDR call records received via CCIS from remote PBX’s.

**M3HP**: Head pointer for SMDR call records received via Fusion from remote PBX’s.

**M3EP** : End pointer for SMDR call records received via Fusion from remote PBX’s.

**CBHP**: Call Base Head Pointer.  Head pointer for idle blocks (empty buffer area).

**CBTP** : Call Base Tail Pointer.  Tail pointer for idle blocks.

**IDL BLK**: Number of Idle Blocks in the buffer (1 block = 144 bytes ; 1 SMDR call record).

**LISC** : Number of SMDR call records from self PBX in buffer. _Note_

        **SCRN **: Number of SMDR call records in buffer that were sent from remote PBX’s via CCIS. _Note_


        **FCBT **: Number of SMDR call records in buffer that were sent from remote PBX’s via Fusion._Note_

_Note: These fields are updated every 256 milliseconds and on the hour._

This page is left blank for your notes

**APPENDIX**

**A**

**<span style="text-decoration:underline;">ATDF : Assignment of Time Difference Data</span>**

    In a Fusion Network if the time between the nodes and the UCT (Universal Coordinated Time) is not identical, this command can be used to set the time difference margin by adding or subtracting hours and minutes.  This data is written into Network Data Memory (NDN) of the Network Control Node (NCN).


     FPC : Fusion Point Code


     SIGN : 


      🡪 1 : Plus (adding)


      🡪 2 : Minus (subtracting) 


     


     HOUR : Hour of time difference (00~12)


     MINUTE : Minute of time difference (00~59)

**APPENDIX**

**B**

**<span style="text-decoration:underline;">DLSD : Display of Lump SMDR Data</span>**

    This command is available in R9 software or higher.


    DLSD is broken into two screens.  ‘SMDR SETTING DATA’ will show various settings in regards to the output and collections of SMDR.  ‘CBT’ will show data stored in the SMDR Buffer.

<p id="gdcalert57" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image57.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert58">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image57.png "image_tooltip")

    MODE : Type of output for SMDR


     🡪 RS232C


     🡪 LAN


    IP ADR : [When MODE=LAN] IP Address of the PBX (_ASYDL Index’s 515~518_)


    SUB NET : [When MODE=LAN] Subnet Address of the PBX (_ASYDL Index’s 519~522_)


    PARITY : [When MODE=LAN] TCP/IP connection parity (_ASYDL Index 529_)


     🡪 NON : No Parity


     🡪 ODD : Odd Parity


     🡪 EVEN : Even Parity


    <p style="text-align: right">
<strong><span style="text-decoration:underline;">DLSD Cond.</span></strong></p>

    SITUATION : Shows how the SMDR devices (0 thru 3, also named ‘A’ thru ‘D’) are configured


     Column One : Device number (where 0 is ‘A’; 1 is ‘B’; 2 is ‘C’; 3 is ‘D’)


     Column Two : How the Device is configured


      🡪 NON : Not configured


      🡪 PORT # : I/O port number that is outputting SMDR


      🡪 OK : Use permission


      🡪 NG : LAN ports used (Use NON permission)


     Column Three : SMDR Format


      🡪 PAST : Normal Format (KA, KB, KE)


          🡪 EXPANSION : Extended Format (KH, KI, KJ) [_Note: Expansion is shown when ASYD Index 288~294 are flagged for Extended Format.  However you will not see an extended record unless Index 296 is flagged as well._)


      🡪 NEXT : IMX Format (KK, KL, KM)


    STA : Station number output type (_ASYDL Index 641, Bit 0_)


     🡪 PHY : Physical Number


     🡪 LOG : Logical / Telephone Number


    RT : Route number output type (_ASYDL Index 641, Bit 3_)


     🡪 PHY : Physical route number


     🡪 LOG : Logical route number


    S.I.S.C : Is Station to Station SMDR ON or OFF


     (_Bugged?  Always says ON.  MAT Version R12 0.26_)


    CBT S.N : SMDR Stored Node?


     🡪 STA : When ASYDL Index 583, Bit 7 = 0


     🡪 TRK : When ASYDL Index 583, Bit 7 = 1


    M.P CBT : [When CBT S.N=STA] Movement Period of SMDR (_ASYDL Index 583_)


    C.B CCIS : Centralized Billing on a CCIS Network (_Determined by ASYD Index’s 182~183_)


     🡪 CENTER : SMDR is not shipped across CCIS


     🡪 LOCAL : SMDR is shipped to a Centralized Node across CCIS


    C.B.P.C : [When C.B CCIS=LOCAL] Centralized Billing Point Code (_ASYD Index’s 182~183_)


    C.B FUSION : Centralized Billing on a Fusion Network, ON or OFF (_ASYDL Index 576_)


    C.FPC : [When C.B FUSION=ON] Fusion Point Code of the Polling Node


    180SE : Is the system an IPX UMG


     🡪 ON : System is an IPX UMG


     🡪 OFF : System is not an IPX UMG


    LMG POL : [When 180SE=ON] Polling Timer for LP’s


    POL CYC : [When C.B FUSION=ON] Polling Cycle Timer (_ASYDL Index 585_)


    POL N.N : [When C.B FUSION=ON] Number of Nodes to be Polled at once (_ASYDL Index 583_)


    FPC P.D : [When C.B FUSION=ON] Chart will show the Fusion Point Codes to be polled as highlighted (_ASYDL Index’s 608~639_)


    PLO STP : Percentage full the buffer must be to stop SMDR Polling (_ASYDL Index 586_)


    **<span style="text-decoration:underline;">DLSD Cond.</span>**

<p id="gdcalert58" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image58.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert59">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image58.png "image_tooltip")

    File Del : [Button] does not appear to do anything???


    CT : SMDR Buffer Counters.  Shows how many records (blocks) are stored in Self, CCIS, and Fusion Buffers; also shows how many blocks are idle.  This is a snapshot, not real time.


    Buffer Selection : [Radio Buttons] select which buffer you wish to view


    Record Selection : 

 🡪 FRONT GET : Will select beginning with the last / newest record

 🡪 BACK GET : Will select beginning with the first / oldest record

             🡪 COUNTER : [Max value is 10] Selects which record to view (e.g. a 4 in this field will display the fourth record in the buffer)


            KIND : Type of call record


             🡪 STA : Station to Station call


             🡪 OG : Outgoing trunk call


             🡪 IC : Incoming trunk call


            OG (1) : [When KIND=OG] Displays the outgoing trunk information from the call record


            OG (2) : [When KIND=OG or STA] Displays the Calling Party information from the call record


            IC (1) : [When KIND=IC] Displays the incoming trunk information from the call record


        IC (2) : [When KIND=IC or STA {if STA this field will be in a different location on the screen}] Displays the Called Party information from the call record


    <p style="text-align: right">
<strong><span style="text-decoration:underline;">DLSD Cond.</span></strong></p>

            ACNT CD : Displays the Forced Account Code from the call record, if present


        DIAL CD : [When KIND=OG or IC] Displays the Called Number from the call record (will only be populated on an Outgoing call)


        AUTH CD : [When KIND=OG or IC] Displays the Authorization Code from the call record, if present (will only be populated on an Outgoing call)


        ANI : [When KIND=OG or IC] Displays the Caller ID / ANI from the call record (will only be populated on an Incoming call)


        C.O.C : [When KIND=OG or IC] Displays the Office Code of the originating PBX (will only be populated on Outgoing CCIS calls)


        C.B.O.C : [When KIND=OG or IC] Displays the Office Code of the terminating PBX (will only be populated on Outgoing CCIS calls)


        START : Displays the billing start time and date


        END : Displays the billing end time and date


        RS232C : Displays which SMDR Devices (0~3 or A~D) are active for serial output


         🡪 Device 0 / A has a value of ‘1’


         🡪 Device 1 / B has a value of ‘2’


         🡪 Device 2 / C has a value of ‘4’


         🡪 Device 3 / D has a value of ‘8’


         Thus if Device 0, 2, and 3 are used this field would display ‘D’ (1+4+8=13 convert to hex = D)


        LAN : Displays which SMDR Devices (0~3 or A~D) are active for TCP/IP output


         🡪 Device 0 / A has a value of ‘1’


         🡪 Device 1 / B has a value of ‘2’


         🡪 Device 2 / C has a value of ‘4’


         🡪 Device 3 / D has a value of ‘8’ 


         Thus if Device 0, 2, and 3 are used this field would display ‘D’ (1+4+8=13 convert to hex = D)


        FUSION : Displays a ‘1’ when records are to be sent across Fusion


        CCIS : Displays a ‘1’ when records are to be sent across CCIS


        CBT ADR : Memory address of the record you are currently viewing


        FRONT ADR : Memory address of the next record


        REAR ADR : Memory address of the previous record


        CBT OUTPUT AREA : Displays the memory area of the record you are currently viewing


        DEL : [Button] 


         🡪 ONLY : Deletes the record you are currently viewing


         🡪 ALL : Deletes the entire buffer

**APPENDIX**

**C**

**<span style="text-decoration:underline;">How to include both Account Codes and Auth Codes in SMDR</span>**

To make both Account Codes [A-18] and Authorization Codes [A-20] appear in the SMDR record; you must enter the Account Code via access code, then dial the number, then enter the Auth Code (Only Account Codes and Procedure 2 Auth Codes will work, Forced Account Codes and Procedure 1 Authorization Codes will not work).

**Programming example**

    ASYD


     System Data 1


      Index 43, Bit 2 = 1 (Send Service Set Tone after access code is entered)


     System Data 2


      Index 3, Bit 4 = 0 (Authorization Codes and Account Codes are NOT used together)


      Index 3, Bit 5 = 0 (Code type is Authorization Code)


    ASPA : assign an access code for the Account Code

 🡪 ACC : *8 (example access code)

 🡪 CI : N (Normal Condition)

 🡪 SRV : SSC

 🡪 SID : 41

 🡪 NND : Enter number of digits for Account Code _plus_ Access Code

  *8 + 12345678 = 10

  Access Code  Account Code  NND

    ASPA : assign LCR access code to prompt for Auth Code


     🡪 ACC : 9 (example access code)


     🡪 CI : N


     🡪 SRV : LCR


     🡪 AH : 1 (prompt for Auth Code)


    AMND : assign number of digits for Authorization Codes


     🡪 TN : 0


     🡪 DC : assign first digit to be used in Auth Codes (example : 7)


     🡪 MND : assign maximum number of digits required for the Auth Code (example : 8)


    AATC : assign the Authorization Code


     🡪 DC : 71234567 (example Auth Code)


     🡪 ACR : 2 (unrestricted) / a setting of ‘1’ to change the RSC of the station will work too


    ASFC : allow Auth Codes to be used by the station


     🡪 SFI 27 : 1 (allowed)


    ARSC : restrict the outgoing route from direct dialing


     🡪 RRI 3 : 2 (toll restriction)

**Dialing Example**

 <span style="text-decoration:underline;">*8</span> <span style="text-decoration:underline;">12345678</span> <span style="text-decoration:underline;">9</span> <span style="text-decoration:underline;">9725182400</span> <span style="text-decoration:underline;">71234567</span>

 Access for Account Code Access Dialed Number Auth Code

 Account Code  for LCR

 (Hear set tone) (Hear dialtone) (Hear dialtone) (Hear stutter tone)

**APPENDIX**

**D**

**<span style="text-decoration:underline;">CPI 3 - OAI Monitored Numbers</span>**

Beginning with the 2400ICS 'H' version software, the SMDR program was made to recognize OAI predictive dial for internal processing as a "Calling Party Identification (CPI) 3."  However, the additional programming was not completed and the project to add this information to SMDR was abandoned.

From 'H' version and up, some part of the SMDR program will still set CPI to a 3.  When this occurs the creation of the SMDR record will be terminated and the now cut off record will be output to the SMDR port.  You will see a record similar to the following example;

```
0!KA025023301....................................001



###                        CPI=3
```

When a SMDR record such as this is encountered, it should be ignored.

**APPENDIX**

**E**

**<span style="text-decoration:underline;">Display Symbol Reference Table</span>**

<p id="gdcalert59" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image59.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert60">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image59.jpg "image_tooltip")
**APPENDIX**

**F**

**<span style="text-decoration:underline;">Blank SMDR Templates</span>**

**Format :**Normal

**Type :**Outgoing

<p id="gdcalert60" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image60.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert61">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image60.jpg "image_tooltip")

        _Note 1 : This field will either contain the first selected route or the ARNP access code of the final selected route._

<p style="text-align: right">
<strong><span style="text-decoration:underline;">Blank SMDR Templates Cont.</span></strong></p>

**Format :**Normal

**Type :**Station to Station

**<span style="text-decoration:underline;">Blank SMDR Templates Cont.</span>**

**Format :**Normal

**Type :**Incoming

<p id="gdcalert61" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image61.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert62">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image61.jpg "image_tooltip")

    _Note : Fields 098~115 may show either the CCIS Office Codes (ARNP Rt. 0) or the Calling Party Number (ANI) depending how ASYD Index's 186 and 241 are assigned;_

<table>
  <tr>
   <td><strong><em>ASYD Index</em></strong>
   </td>
   <td><strong><em>Assignment for Office Code</em></strong>
   </td>
   <td><strong><em>Assignment for ANI</em></strong>
   </td>
  </tr>
  <tr>
   <td><em>186 bit 7</em>
   </td>
   <td><em>1</em>
   </td>
   <td><em>0</em>
   </td>
  </tr>
  <tr>
   <td><em>241 bit 4</em>
   </td>
   <td><em>0</em>
   </td>
   <td><em>1</em>
   </td>
  </tr>
  <tr>
   <td><em>288 bit 5</em>
   </td>
   <td><em>0</em>
   </td>
   <td><em>0</em>
   </td>
  </tr>
  <tr>
   <td><em>296 bit 1</em>
   </td>
   <td><em>0</em>
   </td>
   <td><em>0</em>
   </td>
  </tr>
</table>

_Note : Calling Party Number will be displayed ONLY on the KE generated by an ISDN route.  If the ISDN route tandems across CCIS, the KE generated by the CCIS route will NOT show the Calling Party Number._**<span style="text-decoration:underline;">Blank SMDR Templates Cont.</span>**

**Format :**Expanded

**Type :**Outgoing

**<span style="text-decoration:underline;">Blank SMDR Templates Cont.</span>**

**Format :**Expanded

**Type :**Incoming

<p id="gdcalert62" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image62.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert63">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

![alt_text](images/image62.jpg "image_tooltip")

<p style="text-align: right">
<strong><span style="text-decoration:underline;">Blank SMDR Templates Cont.</span></strong></p>

**Format :**Expanded

**Type :**Station to Station

<!-- Footnotes themselves at the bottom. -->
## Notes

[^1]:

     A node can be any NEAX2400, NEAX2000, or Elite.
