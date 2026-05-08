class Knight:
    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color

    def get_char(self):
        return 'K'

    def can_move(self, horizontal, vertical):
        x1 = ord(self.horizontal) - ord('a') + 1
        x2 = ord(horizontal) - ord('a') + 1
        dx = abs(x2 - x1)
        dy = abs(vertical - self.vertical)
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)

    def move_to(self, horizontal, vertical):
        if self.can_move(horizontal, vertical):
            self.horizontal = horizontal
            self.vertical = vertical

    def get_possible_moves(self):
        offset = [(2, 1),(2, -1),(-2, 1),(-2, -1),
                  (1, 2),(1, -2),(-1, 2),(-1, -2)]

        x = ord(self.horizontal) - ord('a') + 1
        y = self.vertical

        moves = []
        for dx, dy in offset:
            new_x = x + dx
            new_y = y + dy
            if 1 <= new_x <= 8 and 1 <= new_y <= 8:
                new_h = chr(new_x + ord('a') - 1)
                moves.append((new_h, new_y))
        return moves


    def draw_board(self):
        moves = self.get_possible_moves()

        for y in range(8, 0, -1):
            row = []
            for x in range(1, 9):
                h = chr(x + ord('a') - 1)
                if h == self.horizontal and y == self.vertical:
                    row.append(' K ')
                elif (h, y) in moves:
                    row.append(' x ')
                else:
                    row.append(' • ')
            print(''.join(row))

knight = Knight('c', 3, 'white')
knight.draw_board()

