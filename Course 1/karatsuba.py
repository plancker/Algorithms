def karatsuba_multiplier(x, y):
    number1 = list(str(x))
    number2 = list(str(y))
    if len(number1) == 1 or len(number2) == 1:
        return x * y
    else:
        adjustment_factor = 1
        diff_in_lengths = len(number1) - len(number2)


        if diff_in_lengths > 0:
            zeroes = ["0"]*diff_in_lengths
            number2.extend(zeroes)
            adjustment_factor = adjustment_factor*pow(10, diff_in_lengths)
        elif diff_in_lengths < 0:
            zeroes = ["0"]*-diff_in_lengths
            number1.extend(zeroes)
            adjustment_factor = adjustment_factor*pow(10, -diff_in_lengths)
        if len(number1) % 2 != 0 and len(number2) % 2 != 0:
            number1.append("0")
            number2.append("0")
            adjustment_factor = adjustment_factor*100
        elif len(number1) % 2 != 0 and len(number2) % 2 == 0:
            number1.append("0")
            adjustment_factor = adjustment_factor*10
        elif len(number1) % 2 == 0 and len(number2) % 2 != 0:
            number2.append("0")
            adjustment_factor = adjustment_factor*10

        a = int("".join(number1[0:int(len(number1) / 2)]))
        b = int("".join(number1[int(len(number1) / 2):len(number1)]))
        c = int("".join(number2[0:int(len(number2) / 2)]))
        d = int("".join(number2[int(len(number2) / 2):len(number2)]))


        ac = karatsuba_multiplier(a, c)
        bd = karatsuba_multiplier(b, d)
        cross_product = karatsuba_multiplier(a + b, c + d) #=ac + bc + ad + bd
        interim = cross_product - bd - ac # =
        product = 10**len(number1) * ac + 10**(int(len(number1)/2)) * interim + bd
        adjusted_product = product // adjustment_factor
        if adjusted_product != x*y:
            print("Product of", x, " and ", y, " should be ", x*y, " but it comes out to be %f" % adjusted_product)
        return adjusted_product


print(karatsuba_multiplier(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627))
