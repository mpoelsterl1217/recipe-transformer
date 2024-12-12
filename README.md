# recipe-transformer

Public repo link: https://github.com/mpoelsterl1217/recipe-transformer/tree/main

## Requirements

python virtual environment version: 3.12.7

You must have a Java runtime installed on your machine. Install 'requirements.txt' in a virtual environment. Because of the way Windows unzips files, you may encounter an issue where the code has trouble referencing the correct file path. If this happens, make sure to check that the contents of stanford-core-nlp-4.5.7.zip are directly inside a folder with the name stanford-core-nlp-4.5.7/ . This should happen automatically when running the code, but ocassionally Windows unzips the contents into a second subfolder. Feel free to contact us with any questions.

## Instructions

Simply run the interface.py file in a virtual environment to interact with the chatbot. Each time you ask for a transformation, the original version, along with the transformed version, will be saved to a corresponding file in the text_files/ directory. Examples are provided.

## Transformer

We have added features to our chatbot to support recipe transformation. We have implemented the following 

Enter 4 for project 3.

required features:
- change to a vegetarian version ("make it vegetarian")
- change from a vegetarian version ("change it from vegetarian")
- change to Italian cuisine ("make it Italian cuisine")
- make the recipe healthier ("make it healthier")
- revert back to the original recipe ("revert the recipe" or "undo transformations") such as from health

We have also implemented the following optional features:
- double the recipe ("double the recipe")
- half the recipe ("half the recipe")
- scale the recipe by any factor ("scale the recipe")
- change to gluten free ("make it gluten free")
- change to lactose free ("make it lactose free")
- change to Chinese cuisine ("to chinese")


You can find the result of transformer in text_files.

## Previous Features

Previous features are still supported, allowing for inquiries such as:
- Show me the ingredient list.
- What ingredients do I need?
- Where do I begin?
- What is the next step?
- What ingredients do I need for this step?
- What tools do I need for this step?
- What tools do I need for the recipe?
- What methods do I need for this step?
- How much *ingredient* do I need?
- Take me to the 4th step.
- What is the current step?
- Show me the previous step.
- Show me the steps list.
- What temperature?
- How long?
- How do I preheat the oven?
- What can I use instead of oil?

The chatbot is also able to handle many variations of these questions.
We also added the optional part of ingredient and method parsing based on key word list and NLTK.
