# pycoin

    Initial installs:
      --> Install python 3.7 in your system.
      --> Install anaconda-navigator for python 3.7.
      --> Create a new python 3.7 project.
      --> Once installed from the UI of the anaconda-navigator install flask, flask-cors, requests, requests-file.
      
    To run pycoin:
      --> anaconda-navigator
      --> in a new terminal cd /path_to_pycoin
      --> source activate name_of_the_created_project
      --> python3.7 node.py (click on http://0.0.0.0:5000/ that is showing, to open the UI in the default browser 
      automatically 
      or do it manually by opening a browser an typing http://0.0.0.0:5000/.
      --> python3.7 node.py -p a_new_port(e.g.5001 for every new wallet you want to make)   
    
    Pycoin in action:
      Wallet and node segment:
        -->In order to make transactions/mine first you have to create a wallet by clicking on Create New Wallet button.
        -->Load Wallet loads the public and private key of the current node if ti exists.
        -->Recipient key is a field in which a public key is inserted to address the recipint of the coins to send.(you can 
        insert any string like names etc.)
        --> Amount field is the amount to send to the recipient wallet. If the funds of the sender wallet are not enough to 
        make the transaction ,the message 'Creating a transaction failed.' is shown and the transactions fails.
        --> Send button makes the transaction happen.
        Blockchain segment:
          --> Load blockchain button shows each block of the current valid blockchain.
          --> Mine coins button inserts the open transactions in the transaction data of a block and inserts it in the 
          blockchain. The miner is rewarded 10 Pycoins.
          --> Resolve conflicts button is used when 2 wallets are mining new blocks at the same time. Using the consensus
          algorithm the forked blockchain is resolved and the valid one is broadcasted in all the wallets.
        Load Transactions segment:
          --> Load Transactions button shows the open transactions that have not been mined into a block yet
          --> Resolve conflicts button is the same as before
      Network:
        -->Everytime you create a new wallet/node you have to add them both in each others peer nodes in the network segment.
        --> Node url field is used to add peer nodes in the network.(e.g localhost://5001).
        --> Add button adds the peer node into the peer node network
        -->Load peer nodes shown the peers of the current wallet(you can delete them by clicking on them and refreshing the 
        page).
