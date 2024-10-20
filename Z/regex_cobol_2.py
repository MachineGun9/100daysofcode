import re
from collections import defaultdict

cobol_code = """
       IDENTIFICATION DIVISION.
       PROGRAM-ID. ORDERPROCESSOR.

       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT IMS-TRANSACTION-FILE ASSIGN TO IMS-DB.

       DATA DIVISION.
       WORKING-STORAGE SECTION.

       * Include the copybooks for customer and product data
       COPY CUSTOMER-DATA.
       COPY PRODUCT-DATA.

       * MQ Specific fields
       01  MQ-HANDLER.
           05  MQ-MESSAGE-ID      PIC X(24).
           05  MQ-CORREL-ID       PIC X(24).
           05  MQ-MESSAGE         PIC X(256).
           05  ORDER-CUSTOMER-ID  PIC X(10).
           05  ORDER-PRODUCT-ID   PIC X(10).
TEST       05  ORDER-QUANTITY     PIC S9(4) COMP-3.

       * DB2 Specific fields
       EXEC SQL
           INCLUDE SQLCA
       END-EXEC.

       * Message buffer for processing MQ response
       01 RESPONSE-MESSAGE.
           05 RESPONSE-CODE       PIC X(02) VALUE '00'.
           05 RESPONSE-TEXT       PIC X(254).

       PROCEDURE DIVISION.

       * INITIALIZATION SECTION
       INITIALIZATION.
           PERFORM MQ-CONNECT.
           PERFORM MQ-GET-ORDER-MESSAGE.
           PERFORM PROCESS-ORDER.
           PERFORM MQ-SEND-RESPONSE.
           STOP RUN.

       * MQ CONNECTION AND MESSAGE READING SECTION
       MQ-CONNECT.
           DISPLAY 'Connecting to MQ...'.
           * Connect to MQ manager logic here *
           DISPLAY 'Connected to MQ.'.

       MQ-GET-ORDER-MESSAGE.
           DISPLAY 'Getting order message from MQ...'.
           * MQGET logic goes here *
           MOVE '1234567890' TO ORDER-CUSTOMER-ID.
           MOVE 'PROD001' TO ORDER-PRODUCT-ID.
           MOVE 5 TO ORDER-QUANTITY.
           DISPLAY 'Order message received: ' MQ-MESSAGE.

       * ORDER PROCESSING SECTION
       PROCESS-ORDER.
           PERFORM IMS-GET-CUSTOMER-INFO.
           PERFORM DB2-CHECK-INVENTORY.
           IF PRODUCT-STOCK < ORDER-QUANTITY
               MOVE '01' TO RESPONSE-CODE
               MOVE 'Insufficient stock for product' TO RESPONSE-TEXT
               PERFORM MQ-SEND-RESPONSE
               GO TO END-ORDER
           END-IF.
           PERFORM IMS-UPDATE-ORDER-HISTORY.
           PERFORM DB2-UPDATE-INVENTORY.
       END-ORDER.

       * IMS DATABASE PROCESSING SECTION
       IMS-GET-CUSTOMER-INFO.
           DISPLAY 'Reading customer details from IMS...'.
           * Perform IMS transaction read based on ORDER-CUSTOMER-ID *
           MOVE 'John Doe' TO CUSTOMER-NAME.
           MOVE '123 Elm Street' TO CUSTOMER-ADDRESS.
           DISPLAY 'IMS Read completed for CUSTOMER-ID: ' ORDER-CUSTOMER-ID.

       IMS-UPDATE-ORDER-HISTORY.
           DISPLAY 'Updating customer order history in IMS...'.
           * Perform IMS update to customer order history *
           MOVE 'ORD001' TO CUSTOMER-ORDER-HISTORY.ORDER-ID.
           MOVE ORDER-PRODUCT-ID TO CUSTOMER-ORDER-HISTORY.PRODUCT-ID.
           DISPLAY 'IMS Update completed for ORDER-ID: ORD001'.

       * DB2 DATABASE PROCESSING SECTION
       DB2-CHECK-INVENTORY.
           DISPLAY 'Checking product inventory in DB2...'.
           EXEC SQL
               SELECT PRODUCT-STOCK INTO :PRODUCT-STOCK
               FROM PRODUCT_TABLE
               WHERE PRODUCT_ID = :ORDER-PRODUCT-ID
           END-EXEC.
           IF SQLCODE = 0
               DISPLAY 'Product stock: ' PRODUCT-STOCK
           ELSE
               MOVE '1122334455' TO RESPONSE-CODE
                            TEST-VAR
               MOVE 'DB2 error on checking inventory' TO RESPONSE-TEXT
               PERFORM MQ-SEND-RESPONSE
               GO TO END-ORDER.
       
       DB2-UPDATE-INVENTORY.
           DISPLAY 'Updating product inventory in DB2...'.
           EXEC SQL
               UPDATE PRODUCT_TABLE
               SET PRODUCT-STOCK = PRODUCT-STOCK - :ORDER-QUANTITY
               WHERE PRODUCT_ID = :ORDER-PRODUCT-ID
           END-EXEC.
           IF SQLCODE = 0
               DISPLAY 'DB2 inventory update successful.'
           ELSE
               MOVE '99' TO RESPONSE-CODE
               DISPLAY 'DB2 inventory update failed. SQLCODE: ' SQLCODE.

       * MQ RESPONSE SECTION
       MQ-SEND-RESPONSE.
           DISPLAY 'Sending response message to MQ...'.
           IF RESPONSE-CODE = '00'
               MOVE 'Order processed successfully' TO RESPONSE-TEXT
           END-IF.
           * MQPUT logic goes here to send the response *
           DISPLAY 'Response sent: ' RESPONSE-TEXT.

       * END OF PROGRAM
       STOP RUN.

"""
# DATA_FIELDS_PATTERN = (r"^[A-Za-z0-9\s]+(\d{02})\s+([a-zA-Z0-9-]+)\s+[PIC]+\s+([XAS9]+\([0-9]+)\)([^\n]+)|"
#                        r"^[A-Za-z0-9\s]+(\d{02})\s+([a-zA-Z0-9-]+)(\s+)([VALUE]+\s+[A-Za-z0-9'\")]+)")

DATA_FIELDS_PATTERN = (r"^\s*([0-9]{2})\s+([a-zA-Z0-9-]+)\s+(PIC|VALUE)\s+([XAS9]+\([0-9]+\))[^\n]*"
                       r"|^\s*([0-9]{2})\s+([a-zA-Z0-9-]+)\s+(PIC|VALUE)\s+([A-Za-z0-9'\")]+")

# Extracting data fields from the DATA DIVISION
data_fields_pattern = re.compile(DATA_FIELDS_PATTERN, re.MULTILINE|re.IGNORECASE)
data_fields = re.findall(data_fields_pattern, cobol_code)

print(data_fields)

print("Extracted Data Fields:")
for field in data_fields:
    print(field)

X = r"\bMOVE\b\s+([A-Za-z0-9'\"\-@#$%]+)\s+TO\s+([a-zA-Z0-9\-]+.[a-zA-Z0-9-]+)."
# Extracting MOVE statements from the PROCEDURE DIVISION
move_statements_pattern = re.compile(X, re.IGNORECASE)
move_statements = move_statements_pattern.findall(cobol_code, re.IGNORECASE|re.MULTILINE)

print(move_statements)

move_dict = defaultdict(list)
for source, destination in move_statements:
    move_dict[source].append(destination)

print("\nGrouped MOVE Statements:")
for source, destinations in move_dict.items():
    print(f"{source} -> {', '.join(destinations)}")

# Check if each extracted data field is used in the PROCEDURE DIVISION
procedure_division = cobol_code.split("PROCEDURE DIVISION.")[1]
used_fields = [field[0] for field in data_fields if re.search(r'\b' + re.escape(field[0]) + r'\b', procedure_division)]

print("\nData Fields Used in Procedure Division:")
for field in used_fields:
    print(field)

print("\nUnused Data Fields:")
for field in set(data_fields) - set(used_fields):
    print(field)
