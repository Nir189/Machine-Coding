import sys
sys.path.append('/home/isha/Documents/A/P/R/CodingPractice26Jan/CodingPractice/system_design/Machine-Coding/MachineCodingPart1')
from splitwise.controller.user_controller import UserController
from splitwise.controller.group_controller import GroupController
from splitwise.controller.bill_controller import BillController

from splitwise.services.user_service import UserService
from splitwise.services.group_service import GroupService
from splitwise.services.bill_service import BillService

userController = UserController(UserService())
groupController = GroupController(GroupService())
billController = BillController(BillService())

user1 = userController.addUser('user1','Tom')
user2 = userController.addUser('user2','Jerry')
user3 = userController.addUser('user3','Yes')
user4 = userController.addUser('user4','Brok')
user5 = userController.addUser('user5','Misty')

members = [user1,user2,user3,user4,user5]

group = groupController.addGroup('group1','avenger',members)
# print(group.getMembers())
paid_by = {'user1':200,'user2':100,'user3':50,'user4':500,'user5':100}
contribution = {'user1':100,'user2':100,'user3':100,'user4':100,'user5':100}
bill1 = billController.addBill('bill1',group,500,contribution,paid_by)
balance_user1 = billController.getBalance('user1')
print(balance_user1)