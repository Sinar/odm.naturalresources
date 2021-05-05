# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s odm.naturalresources -t test_mining_concession.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src odm.naturalresources.testing.ODM_NATURALRESOURCES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/odm/naturalresources/tests/robot/test_mining_concession.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Mining Concession
  Given a logged-in site administrator
    and an add Mining Concession form
   When I type 'My Mining Concession' into the title field
    and I submit the form
   Then a Mining Concession with the title 'My Mining Concession' has been created

Scenario: As a site administrator I can view a Mining Concession
  Given a logged-in site administrator
    and a Mining Concession 'My Mining Concession'
   When I go to the Mining Concession view
   Then I can see the Mining Concession title 'My Mining Concession'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Mining Concession form
  Go To  ${PLONE_URL}/++add++Mining Concession

a Mining Concession 'My Mining Concession'
  Create content  type=Mining Concession  id=my-mining_concession  title=My Mining Concession

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Mining Concession view
  Go To  ${PLONE_URL}/my-mining_concession
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Mining Concession with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Mining Concession title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
