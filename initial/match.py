def checkStatus(status):
    match(status):
        case "success":
            print("Success")
        case "failure":
            print("Failure")
        case _:
            print("Unknown status")

checkStatus("success")
checkStatus("failure")
checkStatus("error")
