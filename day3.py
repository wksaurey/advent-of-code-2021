import util

def main():
    diag_report = util.read_stripped_lines('input/day3.txt')

    life_support_rating = ''
    ox_gen_rating = find_life_support(diag_report, 1)
    co2_scrub_rating = find_life_support(diag_report, 0)
    print(f'ox: {ox_gen_rating}')
    print(f'co2: {co2_scrub_rating}')

    ox_gen_rating = int(ox_gen_rating, 2)
    co2_scrub_rating = int(co2_scrub_rating, 2)
    print(f'ox: {ox_gen_rating}')
    print(f'co2: {co2_scrub_rating}')

    print(f'lsr: {ox_gen_rating*co2_scrub_rating}')

def find_life_support(lsr_values, rating_type, bit_index=0):
    new_lsr_values = []

    bit_counts = [0, 0]

    for num in lsr_values:
        bit_counts[int(num[bit_index])] += 1

    if bit_counts[0] == bit_counts[1]:
        bit_counts[1] += 1

    if rating_type == 0:
        #co2
        bit_criteria = bit_counts.index(min(bit_counts))
    else:
        # oxgen
        bit_criteria = bit_counts.index(max(bit_counts))
    for num in lsr_values:
        if int(num[bit_index]) == bit_criteria:
            new_lsr_values.append(num)

    if len(new_lsr_values) == 1:
        return new_lsr_values[0]
    return find_life_support(new_lsr_values, rating_type, bit_index+1)

main()