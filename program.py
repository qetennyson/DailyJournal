# import journal - this provides explicit importing
# from journal import load, save - slightly less explicit but understandable
# from journal import * - typically bad practice
import journal

def main():
    print_header()
    run_event_loop()


def print_header():
    print('------------------')
    print('   journal app')
    print('------------------')


def run_event_loop():
    print('What do you want to do with your journal?')
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name)  # []  #  list()

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry, we don't understand '{}'.".format(cmd))

    print('Done, goodbye.')
    journal.save(journal_name, journal_data)


def list_entries(data):
    print('Your journal entries: ')
    entries = reversed(data)
    for index, entry in enumerate(entries):
        print('* [{}] {}'.format(
            index+1, entry))  # index + 1 for humans


def add_entry(data):
    text = input('Type your entry, <enter> to exit ')
    journal.add_entry(text, data)  # a better method of getting the data

    # todo: how to annotate assignments to preserve code improvements
    # data.append(text)  # UI touching the data.  Not desirable.


if __name__ == '__main__':
    main()

