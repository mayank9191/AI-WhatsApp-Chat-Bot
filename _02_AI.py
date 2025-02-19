from groq import Groq


def aiProcess(command):
    client = Groq(
        api_key="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",
    )

    chat_completion = client.chat.completions.create(

        # Required parameters

        messages=[

            # Set an optional system message. This sets the behavior of the
            # assistant and can be used to provide specific instructions for
            # how it should behave throughout the conversation.

            {
                "role": "system",
                "content": "You are an AI assistant emulating Mayank, a Computer Science Engineering student at DTU. Mayank is passionate about coding and enjoys playing guitar, listening to music, and watching movies and series. He is known for being friendly, humorous, and knowledgeable, with a talent for singing. Mayank naturally blends English and Hindi in his speech and comes from South West Delhi. He is empathetic, attentive, and always ready to help others and share knowledge. In any scenario, respond just as Mayank would. Output should be the next chat response (text message only) and remove the date, time and your name  ",
            },
            # Set a user message for the assistant to respond to.

            {"role": "user", "content": command}

        ],

        # The language model which will generate the completion.
        model="llama3-8b-8192",


        #
        # Optional parameters
        #

        # Controls randomness: lowering results in less random completions.
        # As the temperature approaches zero, the model will become deterministic
        # and repetitive.
        temperature=0.5,

        # The maximum number of tokens to generate. Requests can use up to
        # 32,768 tokens shared between prompt and completion.
        max_tokens=1024,

        # Controls diversity via nucleus sampling: 0.5 means half of all
        # likelihood-weighted options are considered.
        top_p=1,

        # A stop sequence is a predefined or user-specified text string that
        # signals an AI to stop generating content, ensuring its responses
        # remain focused and concise. Examples include punctuation marks and
        # markers like "[end]".
        stop=None,

        # If set, partial message deltas will be sent.
        stream=False,
    )

    # return the completion returned by the LLM.
    return (chat_completion.choices[0].message.content)
