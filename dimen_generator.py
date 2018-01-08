print("""available resources\n"""
      """ 1. 962x600 \n"""
      """ 2. 1280x800 \n"""
      """ 3. 1280x900 \n"""
      """ 4. 1024x768 \n"""
      """ 5. 1280x720 \n""")
# print("select default")

# a = int(input())
a = 4

resource_qualifier = ["sw600dp", "sw800dp", "sw900dp",  "sw768dp", "sw720dp" ]

resources = {1: (962, 600),
             2: (1280, 800),
             3: (1280, 900),
             4: (1024, 768),
             5: (1280, 720)}

selected_resource_tuple = resources[a]

default_height, default_width = selected_resource_tuple

resources_ratios = {1: (962 / default_height, 600 / default_width),
                    2: (1280 / default_height, 800 / default_width),
                    3: (1280 / default_height, 900 / default_width),
                    4: (1024 / default_height, 768 / default_width),
                    5: (1280 / default_height, 720 / default_width)}

print("enter resource name")
name = input()
name = name.replace(" ", "_")

print("is dimen width (1) or height(0)?")
index = int(input())

print("enter value as _value_dp or _value_sp")
value = input()
num_value = int(value[0:value.__len__() - 2])
resource_value = value[-2:]


def func():
    resource_text = ""
    for i in range(5):
        val = int(round(resources_ratios[i + 1][index] * num_value))
        resource_text = resource_text \
                        + '<!--{3}-->\n<dimen name="{0}">{1}{2}</dimen>' \
                            .format(name,
                                    val,
                                    resource_value,
                                    resource_qualifier[i])
        resource_text = resource_text + "\n\n"

    print(resource_text)

func()

