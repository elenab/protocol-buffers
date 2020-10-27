import simple.simple_pb2 as simple_pb2

simple_message = simple_pb2.SimpleMessage()
# default values do not show in the message when printing
simple_message.id = 0
assert simple_message.is_simple is False
print(simple_message)

simple_message.id = 123
simple_message.is_simple = True
simple_message.name = "Message one"
print(simple_message)

# simple_message.notexist = "This test should give a runtime error.."
# simple_message.id = "Test wrong type should fail"

simple_list = simple_message.sample_list
# simple_list is a protocol buffer specific object (RepeatedScalarContainer) not an actual list
# but it has all the attributes one would expect from a list
simple_list.append(3)
simple_list.append(34)
simple_list.append(5)
print("---------------")
print(simple_list)
print("---------------")
print(simple_message)
print("---------------")

with open("simple.bin", "wb") as f:
    print("Write bytes to file")
    bytesAsString = simple_message.SerializeToString()
    f.write(bytesAsString)
    print("---------------")

with open("simple.bin", "rb") as f:
    print("Read from file:")
    simple_message_read = simple_pb2.SimpleMessage().FromString(f.read())
    print(simple_message_read)
