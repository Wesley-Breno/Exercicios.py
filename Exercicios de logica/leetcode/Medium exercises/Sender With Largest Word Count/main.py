class Solution:
    def largestWordCount(self, messages: list[str], senders: list[str]) -> str:
        most_words = dict()

        for i in range(0, len(messages)):
            try:
                most_words[senders[i]] += len(messages[i].split())
            except KeyError:
                most_words[senders[i]] = len(messages[i].split())

        ordered_by_value = sorted(dict(most_words).items(), key=lambda item: item[1], reverse=True)

        response = []
        last_value = None

        for user, value in ordered_by_value:
            if len(response) == 0:
                last_value = value
                response.append(user)
                continue

            if value != last_value:
                break

            response.append(user)
            response = [sorted(response)[-1]]

        return response[0]