from item import Item, testing
from phone import Phone
from speaker import Speaker 



item1 = Item("MyItem", 750)

# Item.testing = classmethod(testing)

# Item.testing()
# item1.name = "OtherItem"
# item1.price = -800


# print(item1.read_only_name)
# print(item1.read_only_name) This is for the restricting access for that(Encapsulation)
# print(item1.apply_increment(0.2))
# item1.apply_discount()

# print(item1.price)

# Abstraction
# item1.send_email()

# Inheritance
# phone1 = Phone('jscPhonev10', 500, 5, 1)
# print(phone1.calculate_total_price())
# print(Item.all)
# # print(Phone.all)
# phone2 = Phone('jscPhonev20', 700, 5, 2)

# Item.instantiate_from_csv()
# print(Item.all)

# print(Item.is_integer(9.0))
# item1.apply_discount()
# print(item1.price)

# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)


# print(Item.pay_rate) #Class attributes
# print(item1.pay_rate) #Instance attributes
# print(item2.pay_rate) #Instance attributes

# print(Item.__dict__) # All the attributes of the class level
# print(item1.__dict__) # All the attributes of the instance level

# print(item1.calculate_total_price())
# item2.has_numpad = False

# Polymorphism
# name = "Jim"
# print(len(name))

# some_list = ["some", "name"]
# print(len(some_list))

phone1 = Phone('jscPhonev10', 1000, 5, 1)
phone1.apply_discount()
print(phone1.price)

item1 = Speaker('jscSpeaker', 1000, 5)

item1.apply_discount()

print(item1.price)