from ai.core.ai_engine import AIEngine
from ai.models.llm_provider import MockProvider

engine = AIEngine(MockProvider())

result = engine.generate(
    "أنشئ تطبيق لإدارة مطعم مع لوحة تحكم حديثة"
)

print(result)
