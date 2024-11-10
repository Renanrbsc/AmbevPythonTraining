def convert_number_in_bynary(number):
	binary = bin(int(number))
	print(f"O numero convertido em binario: {binary}")
	return binary[2:]


def looking_for_spaces_between_binary(binary):
	binary_number_to_split_in_list = binary.split('1')
	binary_number_to_split_in_list.pop()
	list_max_number_space = []
	for split in binary_number_to_split_in_list:
		list_max_number_space.append(len(split))

	print(f"O maior numero de espaços na lista é: {max(list_max_number_space)}")


number = input("Informe um numero: ")
number_binary = convert_number_in_bynary(number)
looking_for_spaces_between_binary(number_binary)
