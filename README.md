# portfolio-student-discount
Python practice of digital bootcamp with School of Computing & Mathematics, MMU. 
1.	A coffee shop offers students 10% discounts on things they buy. This program accepts user input for the cost of an item (e.g. 10.00) and the status of the user (“student” or “staff”). The program follows the following requirements.
-	If the user is a staff member, the user will be charged the full amount
-	Otherwise, if the user is a student, the user gets 10% off the price
-	Otherwise, if the user status is not “student” or “staff” the user is charged the full amount
2.	Display the amount to be paid on the screen
3.	If the user’s status is NOT “student” or “staff”, display the user is unknown and does not qualify for any discount.

Summary:
After a user enters the status of student, staff or others, there are three conditional
blocks to decide which result will display according to the user’s status. The three
results will be having a 10% discount of the purchase, without discount and without
discount by showing that the user is not qualified for any discount.

Self-reflection:
I found that str in the input command could decide if the user has entered the proper
status or not in order to show a corresponding result. Besides, I have added an extra
conditional requirement to include the possibility that users may enter status with
capital or small letters.
