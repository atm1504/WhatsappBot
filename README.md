# WhatsappBot
Whatsapp bot made using python3 and selenium

To use the script, install the following dependencies first:
* Selenium
* Chrome Web Driver (mac version already provided inside driver folder)

## Bots Developed 
* Bot to spy on a friend. This bot spies when you friend goes online and when he/she goes offline.
* An AI (can be used without smart reply also) based bot to chat with a friend.
* A bot to reply users whenever someone texts you.
* A bot to send a message multiple time.
* A bot to reply your friends whenever they replies on your WhatsApp status.

### Script to message someone (simple_message.py)
* Specify the chrome driver path while initializing Chrome
* Write the target name in the target variable
* Execute ```python3 simple_message.py```

### Script to keep an eye on a user (onlineState.py)
* Specify the chrome driver path while initializing Chrome
* Write the target name in the target variable
* Choose the last seen visibility of the user
* Execute ```python3 onlineState.py```

### Script to reply messages of an user (messageReply.py)
* Specify the chrome driver path while initializing Chrome
* Write the target name in the target variable
* Execute ```python3 messageReply.py```e

### Script to auto reply message to the users who sends u a new message (newMessageReply.py)
* Specify the chrome driver path while initializing Chrome
* Execute ```python3 newMessageReply.py```

Here, I have used ```Microsoft Azure QnA Maker``` to make give smart replies. You can also it. If you don't want to make use of AI bots then simply adjust this to values ```ans = getAnswer(lm_text); sendMessage(ans)``` in the file.
To use the bot, follow the steps mentioned in this doc https://docs.microsoft.com/en-us/azure/cognitive-services/QnAMaker/Quickstarts/create-publish-knowledge-base#create-a-bot .
Make suitable changes in the file. Add the API_KEY and the url. Feel free to use it.

### Screen Shots
Note: Actual output pattern may differ.
![1](https://user-images.githubusercontent.com/43731599/79439894-ffe17400-7ff2-11ea-9f12-1076a34a1d30.jpeg)
![2](https://user-images.githubusercontent.com/43731599/79439903-0374fb00-7ff3-11ea-88da-a4b6e513841e.jpeg)
![3](https://user-images.githubusercontent.com/43731599/79478102-9ed49300-8028-11ea-9f71-8f9e1bafbcbe.jpg)
![ezgif com-video-to-gif](https://user-images.githubusercontent.com/43731599/79620034-3ec71500-812c-11ea-9f02-948834162a94.gif)
![gif22323](https://user-images.githubusercontent.com/43731599/79667353-9b313f80-81d3-11ea-836e-da106ae199da.gif)
![gif](https://user-images.githubusercontent.com/43731599/79632685-93937b80-817e-11ea-83d4-bc4f43e1e08e.gif)
![test1](https://user-images.githubusercontent.com/43731599/79477953-72b91200-8028-11ea-9395-e6837b5eb1a1.jpeg)

