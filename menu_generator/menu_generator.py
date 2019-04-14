# Author: Akshay Naik

class menu_generator:
    def list_menus(self, n_cus, n_dish):
        if n_cus==0 or n_dish==0:
            return []

        menu = []
        self.helper(n_cus, [i for i in range(n_dish)], 0, 0, [], menu)

        return menu

    def helper(self, n_cus, n_dish, c_index, d_index, cur, menu):
        if len(cur)== n_cus:
            menu.append(cur)
            return

        for i in range(c_index, n_cus):
            for j in n_dish:
                self.helper(n_cus, n_dish, i+1, j+1, cur[:]+[chr(65+i)+str(j+1)], menu)

# Input to function
t = menu_generator()
print (t.list_menus(2,2))
