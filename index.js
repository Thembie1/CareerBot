require('dotenv').config();

// The OpenAI library is needed to make API calls.
const OpenAI = require('openai');

const openai = new OpenAI();

async function main() {
  try {
    console.log('Sending request to OpenAI...');
    
    const chatCompletion = await openai.chat.completions.create({
      model: 'gpt-3.5-turbo',
      messages: [{ 
        role: 'user', 
        content: 'What is the capital of South Africa?' 
      }],
    });
    
    console.log('\nOpenAI response:');
    console.log(chatCompletion.choices[0].message.content);
    
  } catch (error) {
    console.error('\nAn error occurred while calling the OpenAI API:');
    console.error(error);
  }
}

main();