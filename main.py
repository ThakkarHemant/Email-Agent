from agent.email_agent import run_email_agent

if __name__ == "__main__":
    user_input = input("Enter your email prompt: ")
    response = run_email_agent(user_input)
    print("\nGenerated Email:\n")
    print(response)
