def numUniqueEmails(emails):
    unique = set()
    for email in emails:
        i = 0
        local = ''
        while email[i] != '@':
            if email[i] == '.':
                i += 1
                continue
            elif email[i] == '+':
                break
            else:
                local += email[i]
                i += 1
        unique.add(local + email[email.find('@'):])
    return len(unique)


print(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))

def strip(email):
    local = email[:email.find('@') + 1].replace('.', '')
    if local.find('+') == -1:
        local = local[:local.find('+')]
    return local

def popletter(str, letter):
    for s in str:
        if s == letter:
            str.remove(s)