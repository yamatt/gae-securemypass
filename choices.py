
def remove_score(options):
    return map(lambda (key, values): (key, values[0]), options['questions'].items())


HASHES = {
    "name": "Hashing",
    "id": "hashing",
    'questions': {
        'no': ('No', 3),
        'sha1': ('SHA-1', 2),
        'sha256': ('SHA-256', 1),
        'sha512': ('SHA-512', 1),
        'md5': ('MD5', 2),
        'bcrypt': ('bcrypt', 0),
        'scrypt': ('scrypt', 0),
        'custom': ('Custom', 2)
    },
    'results': [
        """bcrypt and scrypt are about the best hasing tools out there. This doesn't mean it can't be broken, but at least if you were breaking passwords in bulk it's going to take significatnly longer than other means.""",
        """Not a bad start. Although these hashing algroythems are very strong you get advantages with bcrypt and scrypt such as running them""",
        """SHA-1 and MD5 hashes are notoriously broken. Even the creator of said hashes has said so himself. Rolling your own hashing algorythem is also a bad idea because you don't know how broken it is.""",
        """This is a BAD idea. Unenrypted passwords are a huge security lapse. Especially when it is so easy to apply a modicome of security. Think about the expense Sony had to deal with when their PSN network went down.""",
    ]
}

SALTING = {
    "name": "Salting",
    "id": "salting",
    "questions": {
        'no': ('No', 2),
        'yes-one': ('Yes - One Salt', 1),
        'yes-individual': ('Yes - Salt per Password', 0)
    },
    "results": [
        """This is the best way to do things. Assuming the password is strong to start off with this makes brute forcing the passwords very slow. ((Stats how long to break))""",
        """That's a pretty good effort, but let's say your salt is discovered as well as your passwords the hashes can then be brute forced in bulk. ((Stats how long to break))""",
        """This is pretty much the worst thing to do. There was public out-cry when last.fm didn't salt their passwords. It means brute forcing passwords in bulk will result in broken passwords very quickly.((Stats how long to break))""",
    ]
}

EMAILING = {
    "name": "Emailing",
    "id": "emailing",
    "questions": {
        'no': ('No', 0),
        'yes': ('Yes', 1)
    },
    "results": [
        """It is a very good idea to send passwords through unencrypted mediums. But then you already knew that.""",
        """A lot of websites seem to think this is a good idea, but think about the e-mail system for a second. It consists of an un-determinable number of hops, none of it is encrypted. Any one of those hops could potentially gather that password and completely by-pass any security measure you may put in place in your database."""
    ]
}
