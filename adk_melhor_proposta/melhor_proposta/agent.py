from . import prompts
from . import tools
from google.adk.agents import Agent


modelo = "gemini-2.0-flash"

boas_vindas = Agent(
    name="boas_vindas",
    model=modelo,
    description="Você dá boas-vindas a pessoa usuária sempre depois do gatilho 'Olá'",
    instruction=prompts.recepcionando,
    tools=[],
    output_key="boas_vindas_resultado"
)

precifica = Agent(
    name="precifica",
    model=modelo,
    description="Você precifica o projeto, esperando a sua vez depois do agente boas_vindas",
    instruction=prompts.precificando,
    tools=[tools.acarv],
    output_key="precifica_resultado"
)

zopa = Agent(
    name="zopa",
    model=modelo,
    description="Você identifica o melhor acordo possível, esperando a sua vez depois do agente precifica",
    instruction=prompts.negociando,
    tools=[],
    output_key="zopa_resultado"
)

relaxa = Agent(
    name="relaxa",
    model=modelo,
    description="Você dá dicas para evitar a insegurança na negociação, esperando a sua vez depois do agente zopa",
    instruction=prompts.acalmando,
    tools=[],
    output_key="relaxa_resultado"
)

melhor_proposta = Agent(
    name="melhor_proposta",
    model=modelo,
    description="""Você organiza os agentes para interagirem em sequência, mas sempre esperando o comando 'next' da 
    pessoa usuária para transferir ao próximo agente""",
    instruction=prompts.coordenando,
    sub_agents=[boas_vindas, precifica, zopa, relaxa]

)

root_agent = melhor_proposta