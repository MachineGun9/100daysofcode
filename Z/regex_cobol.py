import re

cobol_code = """
IDENTIFICATION DIVISION.
PROGRAM-ID. MQIMSDB2.

ENVIRONMENT DIVISION.
CONFIGURATION SECTION.
INPUT-OUTPUT SECTION.
FILE-CONTROL.
    SELECT IMS-TRANSACTION-FILE ASSIGN TO IMS-DB.

DATA DIVISION.
WORKING-STORAGE SECTION.

* MQ Specific fields
01  MQ-HANDLER.
    05  MQ-MESSAGE-ID      PIC X(24).
    05  MQ-CORREL-ID       PIC X(24).
    05  MQ-MESSAGE         PIC X(256).
BOB 05  MQ-TEST                               
                           PIC 9(1).    

* DB2 Specific fields
EXEC SQL
    INCLUDE SQLCA
END-EXEC.
01 DB2-CUSTOMER-INFO.
    05 CUSTOMER-ID         PIC X(10).
    05 CUSTOMER-NAME       PIC X(30).
    05 ACCOUNT-BALANCE     PIC S9(7)V99 COMP-3.

* IMS Specific fields
01 IMS-SEGMENT.
    05 CUSTOMER-ID         PIC X(10).
    05 CUSTOMER-DETAILS    PIC X(100).

* Message buffer for processing MQ response
01 RESPONSE-MESSAGE.
    05 RESPONSE-CODE       PIC X(02) VALUE '00'.
    05 RESPONSE-TEXT       PIC X(254).

PROCEDURE DIVISION.

* INITIALIZATION SECTION
INITIALIZATION.
    PERFORM MQ-CONNECT.
    PERFORM MQ-GET-MESSAGE.
    PERFORM IMS-READ.
    PERFORM DB2-UPDATE.
    PERFORM MQ-SEND-RESPONSE.
    STOP RUN.

* MQ CONNECTION AND MESSAGE READING SECTION
MQ-CONNECT.
    DISPLAY 'Connecting to MQ...'.
    * Connect to MQ manager logic here *
    DISPLAY 'Connected to MQ.'.

MQ-GET-MESSAGE.
    DISPLAY 'Getting message from MQ...'.
    * MQGET logic goes here *
    MOVE '1234567890' TO CUSTOMER-ID.
    DISPLAY 'Message received: ' MQ-MESSAGE.

* IMS DATABASE PROCESSING SECTION
IMS-READ.
    DISPLAY 'Reading customer details from IMS...'.
    * Perform IMS transaction read based on CUSTOMER-ID *
    MOVE 'John Doe, Age 35, Location X' TO CUSTOMER-DETAILS.
    DISPLAY 'IMS Read completed for CUSTOMER-ID: ' CUSTOMER-ID.

* DB2 DATABASE PROCESSING SECTION
DB2-UPDATE.
    DISPLAY 'Updating DB2 database with customer balance...'.
    EXEC SQL
        UPDATE CUSTOMER_TABLE
        SET ACCOUNT_BALANCE = ACCOUNT_BALANCE + 100
        WHERE CUSTOMER_ID = :CUSTOMER-ID
    END-EXEC.
    IF SQLCODE = 0
        DISPLAY 'DB2 update successful.'
    ELSE
        MOVE '99' TO RESPONSE-CODE
        DISPLAY 'DB2 update failed. SQLCODE: ' SQLCODE.

* MQ RESPONSE SECTION
MQ-SEND-RESPONSE.
    DISPLAY 'Sending response message to MQ...'.
    MOVE 'Success: Customer updated' TO RESPONSE-TEXT.
    * MQPUT logic goes here to send the response *
    DISPLAY 'Response sent: ' RESPONSE-TEXT.

* END OF PROGRAM
STOP RUN.
"""
A = r"(^\s*|^[a-zA-Z0-9]+\s+)[0-9]{2}\s+([A-Z0-9-]+)\s+PIC\s(X|9)[\s|\(]([0-9]+)\)."
# Extracting data fields from the DATA DIVISION
data_fields_pattern = re.compile(A, re.MULTILINE)
data_fields = re.findall(data_fields_pattern, cobol_code)


print("Extracted Data Fields:")
for field in data_fields:
    print(field[1])

# Check if each extracted data field is used in the PROCEDURE DIVISION
procedure_division = cobol_code.split("PROCEDURE DIVISION.")[1]
used_fields = [field[1] for field in data_fields if re.search(r'\b' + re.escape(field[1]) + r'\b', procedure_division)]

print("\nData Fields Used in Procedure Division:")
for field in used_fields:
    print(field)

print("\nUnused Data Fields:")
for field in set(data_fields) - set(used_fields):
    print(field[1])
