import jinja2

env = jinja2.Environment()

template = env.from_string("Hello {{ name }}")
print(template.render(name="pes"))

