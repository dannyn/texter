

Texter
------

Texter is a program which allows you to send templated text to a list of phone numbers. 

To use it you will need a Apple laptop and an iphone. You will need [text forwarding](https://support.apple.com/en-us/HT208386) turned on. 

The list of numbers are stored in a CSV file, with the phone number first and templated parameters after. 

```
2125551212, name, blue
2125551313, name2, green
```

The message you want to send is stored in another file. You use `{}` to indicate where you want a parameter substituted.

```
Hello {}. Your favorite color is {}.
```

This would send

```
Hello name. Your favorite color is blue. 
```

to 2125551212. 

To invoke the program, 

```
$ python3 list_of_numbers_file message_file
```

Note there is a 30 second delay. If you send texts too quickly Messages appears to throttle them. I could not find out exactly how it works, but did not encounter any issues with 30 seconds.

