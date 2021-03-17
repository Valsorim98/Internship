
class AccessControl():
    """Access control
    """

    __card_reader = None
    """Card reader instance.
    """

    __tokens_base = None
    """Tokens database instance.
    """
 
    def __init__(self, card_reader, tokens_base):
        """Constructor

        Args:
            card_reader (ACT230): Instance of the card reader to work with.
            tokens_base (dict): Tokens database.
        """
    
        self.__card_reader = card_reader

        self.__tokens_base = tokens_base

        if self.__card_reader is not None:
            self.__card_reader.set_card_cb(self.__card_reader_cb)

    def __card_reader_cb(self, card_id):

        if self.__tokens_base is None:
            return

        print(card_id)

        if card_id == "6E536046010080FF":
            print("Access granted.")
        else:
            print("Access denied.")

        #check for code from whitelist in database
        #if not in whitelist its in blacklist


    def update(self):

        if self.__card_reader is not None:
            self.__card_reader.update()
