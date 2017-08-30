
Usage:
•	Through CLI: QueryIPInfo.py IP-ADDRESS (e.g. 8.8.8.8)

Dependencies:
•	This script requires pip installation of: requests, ipaddress

Assumptions:
•	If partial information returns from the server, we will not throw an exception but rather present the information that was given and set in missing information cells the value “No information was given” (can happen due to IPV6).
	  
•	By “returns the above table in markdown” instruction on the exercise I assumed we should write it into a file with a “.md” suffix so I did that with a file called “ip_information.md”.

Design choices:
•	I decided to create a few abstract classes such as “Parser” and “Formatter” to keep the code as generic as possible, the reason for that is to keep the code flexible.  If in the future, we will want to parse a response from the server that is in XML format all we’ll have to do is create a class called “XMLParser” and inherit the Parser class and implement the “parse” method and inject it to the “IPInfo” class and other than that not to touch the other class. Same for the “Formatter” abstract class and the “MarkdownFormatter” that implements it.

•	I decided to decouple the object that holds the information from the object that formats the information and that is the reason that the “Formatter” and the ‘MarkdownFormatter” class exists.
   


