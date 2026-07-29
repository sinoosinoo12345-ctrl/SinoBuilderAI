from ai.core.spec_generator import SpecificationGenerator

generator = SpecificationGenerator()

spec = generator.generate(
    "تطبيق إدارة مطعم"
)

print(spec)
