#Chat bot using patterns

from nltk.chat.util import Chat, reflections

pairs = [
    ['my name is (.*)', ['hi %1']],
    ['(hi|hello|hey|holla|hola)', ['hey there', 'hi there', 'haayyy']],
    ['(.*) in (.*) is fun', ['%1 in %2 is indeed fun']],
    ['(.*)(location|city)?', ['Tokyo, Japan']],
    ['(.*) created you?', ['Joe did using NLTK']],
    ['how is the weather in (.*)', ['the weather in %1 is amazing']],
    ['(.*)help(.*)', ['I can help you']],
    ['(.*) your name', ['My name is Bobby Bushay']]
]

myDummyReflections = {
    'go' : 'gone',
    'hello' : 'hey there'
}
chat = Chat(pairs, myDummyReflections)
#chat._substitute('you are amazing go' )
chat.converse()
