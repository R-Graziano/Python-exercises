import time

class Client:
    def __init__(self, name, time_to_anger):
        self.name = name
        self.time_to_anger = time_to_anger
        self._start_time = time.perf_counter()
        self._elapsed_time = None
        print('{} is sit and waiting...!'.format(self.name))
    
    # hacer el timer para cada cliente, inicia cuando se ejecuta el programa, finaliza cuando termina el deliver.
    def isAngry(self):
        if self._elapsed_time >= self.time_to_anger:
            return ' but is angry.'
        else:
            return ' and is happy.'
    
    def hasOrder(self):
        self._elapsed_time = time.perf_counter() - self._start_time
        print('{} has the order...{} He waited for {} (anger at {}).'
        .format(self.name, self.isAngry(), self._elapsed_time, self.time_to_anger))


def servingOrder(client, timer):
    print('Taking {} order...'.format(client.name))
    time.sleep(timer[0])
    print('Preparing {} order...'.format(client.name))
    time.sleep(timer[1])
    print('Delivering {} order...'.format(client.name))
    time.sleep(timer[2])
    client.hasOrder()


startTime = time.perf_counter()
client_1 = Client('Client_1', 50)
client_2 = Client('Client_2', 20)
client_3 = Client('Client_3', 30)
client_4 = Client('Client_4', 35)
client_5 = Client('Client_5', 35)

servingOrder(client_1, [10, 35, 1])
servingOrder(client_2, [5, 7, 1])
servingOrder(client_3, [10, 20, 1])
servingOrder(client_4, [5, 5, 1])
servingOrder(client_5, [2, 4, 1])

print('The restaurant took {} seconds to serve all orders'.format(time.perf_counter() - startTime))