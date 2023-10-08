alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
          14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
print("We Decrypt and Encrypt Words.")  
print("For Encryption, you enter numbers and we convert it into words.") 
print("And for Decryption, you enter words and we convert it into numbers. \n")       
choice = input("Do you want to Encrypt or Decrypt? Enter 'e' for encryption and 'd' for decryption: ")
if choice == 'e':
 conversion = []
 input1 = input("Enter words : ")
 for char in input1:
     if char.isspace():
         conversion.append('_')
     elif char.isalpha():
         index = alphabet.index(char.lower())
         conversion.append(number[index])
     else:
      conversion.append(char)
 print("\nYour encrypted version of information:")
 print(*conversion, sep=' ')

elif choice ==  'd':
 input1 = input("Enter numbers: ")
 numbers = input1.split()
 
 output = []
 for num in numbers:
     if num.isdigit() and 1 <= int(num) <= 26:
         output.append(alphabet[int(num)-1])
     elif num == '_':
         output.append(' ')
     else:
      output.append(num) 
 print("\nYour decrypted version of information: ")
 print(''.join(output))
 