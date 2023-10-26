import os
os.environ['OPENAI_API_KEY'] ='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'

import os
import openai
openai.organization = "org-X7o4rZjiIb8XcRa6JgGuQKt4"
openai.api_key = os.getenv("OPENAI_API_KEY")
models = openai.Model.list()
print(models)