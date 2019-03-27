from collections import OrderedDict

from utility.printable import Printable


class Transaction(Printable):
    """A transaction which can be added to a block in the blockchain."""

    def __init__(self, txid, sender, recipient, signature, amount, inputs, outputs):
        self.txid = txid
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = signature
        self.inputs = inputs
        self.outputs = outputs

    def to_ordered_dict(self):
        """Converts this transaction into a (hashable) OrderedDict."""
        return OrderedDict([('sender', self.sender),
                            ('recipient', self.recipient),
                            ('amount', self.amount)])
