
# Book-Recommendation-Bot

## Description

This is a simple `book recommendation bot` built using [`Amazon Lex`](https://aws.amazon.com/lex/), integrated with a [`Lambda function`](https://github.com/aakanksha-k/Book-Recommendation-Bot/blob/main/lambda_function.py), to return personalized book suggestions to the users. 

This bot has been deployed on two services, [`kommunicate`](https://www.kommunicate.io/) & [`Twilio`](https://www.twilio.com/en-us)

1. With kommunicate, the chatbot was embedded into an HTML website & the delivery of the chatbot's responses to users was managed, through the web interface.
2. Whereas on Twilio, the delivery of the bot's responses to users via the chosen communication channel, here, `WhatsApp`, was managed. 


## Architecture


![Proj 1_cloud](https://github.com/aakanksha-k/Book-Recommendation-Bot/assets/136099041/2b62af6a-133f-4434-a668-598c3a090fef)


## Services used 🛠 
[`Amazon Lex`](https://aws.amazon.com/lex/)
[`AWS Lambda`](https://aws.amazon.com/lambda/)
[`AWS IAM`](https://aws.amazon.com/iam/)


## Deployment

#### Step 1: Set Up Amazon Lex
1.	Sign in to [`AWS Management Console`](https://aws.amazon.com/console/)

2.	Create a Lex Bot 
- Click on "Create bot."
- Choose "Custom bot" and provide the following details:
-	Bot name: BookRecommendationBot
-	Language: English (or your preferred language)
-	Output voice: None (since it's a text bot)
-	Session timeout: 5 minutes (default)
- COPPA: No
- IAM role: Create a new role with basic permissions
- Sentiment analysis: No

3.	Add `Intents`:
-	Click on "Create intent."
-	Intent name: WelcomeIntent
-	Sample utterances: Add various ways users might ask for a recommendation, e.g., "Can you recommend a book?", "book recommendations", "Suggest a book", , “Hello”

4.	Define `Slots`:
-	Slot name: Genre
-	Slot type: AMAZON.BookGenre (Since, this SlotType isn’t provided by AWS, create a new type)
-	Prompt: "What genre of books do you like?"

5.	Save the Intent and Build the Bot

#### Step 2: Create Lambda Function for Recommendations
1.	Navigate to [`Lambda Console`](https://console.aws.amazon.com/lambda/home)

2.	Create a Function:
-	Click "Create function."
-	Choose "Author from scratch."
-	Provide the following details:
    - Function name: BookRecommendationFunction
    - Runtime: `Python 3.8` (or your preferred runtime
    - Permissions: Choose an existing role or create a new one with basic Lambda permissions.

3.	Add Code:

- Replace the default code with [`lambda_function.py`](https://github.com/aakanksha-k/Book-Recommendation-Bot/blob/main/lambda_function.py)

4.	Deploy the Function

5.	Add Lambda Trigger in Lex:

-	Go back to your Lex bot.
-	In the Intent, scroll to Fulfillment and enable it.
-	Click "Save intent" and "Build."

6.	Deployment:

- Under Deployment, go to Aliases. 
-	Choose the Alias associated with the Bot & select Bot's language.
-	Choose the Source & latest Lambda function and Save the settings. 

#### Step 3: Ensuring User Permissions with IAM

1. Navigate to [`IAM Dashboard`]()

2. Visit Roles > Your-Bot

3. Under Permission Policies
-	Create an inline policy, namely, LexInvokeLambdaPolicy & add the code from [`iam_permissions.json`](https://github.com/aakanksha-k/Book-Recommendation-Bot/blob/main/iam_permissions.json) 
-	Save changes

#### Step 4: Building & Testing

1. Go back to your Lex bot & build

2. Test the bot in `Lex Console`
![Screenshot (946)](https://github.com/aakanksha-k/Book-Recommendation-Bot/assets/136099041/6ad7fbdf-f6f0-413c-8842-92711d5fc207)


#### Step 5: Deployment

#### 5.1 Integrating Amazon Lex with kommunicate

1. Obtain AWS Credentials:
- Sign in to AWS console as Root/IAM user.
- Open IAM panel > "Access management -> Users".
- Create a user (e.g., “Lex-bot”).
- Attach policies: `AmazonLexReadOnly` and `AmazonLexRunBotsOnly`.
- Create Access Key: Select "Third-Party Service" and generate keys.

2. Gather Lex Bot Details:
   - **Bot Name**: Name of your Lex bot.
   - **Bot Alias**: Alias created when publishing the bot.
   - **AWS Region**: Region where Lex service is running.

3. Integrate Lex Bot with Kommunicate:
-  Log in to [`kommunicate`](https://www.kommunicate.io/) > Bot section.
- Click "Integrate Bot" in Amazon Lex card.
- Fill in Access Key ID, Secret Access Key, Bot Name, Bot Alias, AWS Region.
   - Click "Next".

4. Configure Bot in Kommunicate:
- Name your bot (visible to users).
- Enable/Disable "autoHandoff".
- Select "Let this bot handle all new conversations".

5. Set Welcome Message in Lex:
   - Add `kmConversationStarted` as sample utterance to WelcomeIntent.

Once integrated, the HTML website embedded with Lex-bot would look like:
![Screenshot (951)](https://github.com/aakanksha-k/Book-Recommendation-Bot/assets/136099041/7b51b896-ce7b-43cd-be47-dcae47195650)

#### 5.2 Integrating Amazon Lex with Twilio

1. Set Up Twilio Account
  - Sign up at [`Twilio`](https://www.twilio.com/en-us)
  - Obtain your Account SID and Auth Token.
  - Verify your phone number in the Twilio console under "Verified Caller IDs".

2. Create Bot Version and Alias in Lex:
-  Go to your Lex bot and create a new version.
  - Create an alias for the bot and link it with the new version.

3.  Configure Twilio Messaging Service:
  - Access the `Twilio console` and navigate to "Messaging."
  - Set up a messaging service and take note of the assigned phone number.
  - Verify your WhatsApp number following Twilio's sandbox setup.

4. Integrate Lex with Twilio
  - Navigate to "Channels" in the Lex console and add a Twilio channel.
  - Enter your `Twilio Account SID` and `Auth Token`
  -  Copy the callback URL provided by Lex.
  -  In Twilio, set the webhook URL (callback URL from Lex) in the messaging service.

5. Test the Integration
  - Send a message from your verified `WhatsApp` number to the Twilio number.
  - Confirm reception of responses from the Lex bot to validate the integration.

After deployement, the conversation over the chosen communication channel, could look like:
![Screenshot (952)](https://github.com/aakanksha-k/Book-Recommendation-Bot/assets/136099041/18f49c6f-dac8-4841-a1d0-1f0c6824b7b9)
