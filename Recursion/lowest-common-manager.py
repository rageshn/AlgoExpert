"""
 You're given three inputs, all of which are instances of an OrgChart class that have a directReports property pointing
 to their direct reports. The first input is the top manager in an organizational chart (i.e., the only instance
 that isn't anybody else's direct report), and the other two inputs are reports in the organizational chart.
 The two reports are guaranteed to be distinct.
 Write a function that returns the lowest common manager to the two reports.
"""

# Recursive approach
# Time: O(n) | Space: O(d)
##########################
# Declare a class --> OrgInfo
#   Init method takes two arguments lowest_common_manager, num_important_reports
#       Arguments are set to class properties
#
# Call get_org_info method by passing top manager and two reports. This will return the OrgInfo object --> get_org_info(topManager, reportOne, reportTwo)
# return lowest_common_manager in OrgInfo object
#
# Declare a function --> get_org_info(manager, report_one, report_two)
#   Initialize num_important_reports = 0
#   Loop through each reporting person in manager.directReports
#       Recursively call get_org_info by passing reporting person and two reports to find --> org_info
#       If org_info.lowest_common_manager is not Null
#           return org_info
#       Set num_important_reports = num_important_reports + org_info.num_important_reports
#   If manager is either one of two reporting person to find
#       Increment num_important_reports by 1
#   If num_important_reports = 2
#       Set lowest_common_manager = manager
#   else
#       Set lowest_common_manager = Null
#   Create OrgInfo object with lowest_common_manager & num_important_reports
#   return the OrgInfo object
##########################


def getLowestCommonManager(topManager, reportOne, reportTwo):
    org_info = get_org_info(topManager, reportOne, reportTwo)
    return org_info.lowest_common_manager


def get_org_info(manager, report_one, report_two):
    num_important_reports = 0
    for report in manager.directReports:
        org_info = get_org_info(report, report_one, report_two)
        if org_info.lowest_common_manager is not None:
            return org_info
        num_important_reports += org_info.num_important_reports

    if manager == report_one or manager == report_two:
        num_important_reports += 1
    lowest_common_manager = manager if num_important_reports == 2 else None
    return OrgInfo(lowest_common_manager, num_important_reports)


class OrgInfo:
    def __init__(self, lowest_common_manager, num_important_reports):
        self.lowest_common_manager = lowest_common_manager
        self.num_important_reports = num_important_reports


class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
