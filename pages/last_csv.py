class LastCsv:
    @classmethod
    def lastcsv(cls,n,n2):
        first_tuple_el = n
        second_tuple_el = n2
        return cls.chek(first_tuple_el),cls.chek(second_tuple_el)

    @classmethod
    def chek(cls,n):
        transactions_prov1_chek = n.replace(",", "")
        transactions_prov1_chek_1 = transactions_prov1_chek.split()
        first_str = transactions_prov1_chek_1[1] + " " + transactions_prov1_chek_1[0] + " " + transactions_prov1_chek_1[
            2] + " " + transactions_prov1_chek_1[3]
        second_str = transactions_prov1_chek_1[-2]
        theard_str = transactions_prov1_chek_1[-1]
        return first_str,second_str,theard_str

