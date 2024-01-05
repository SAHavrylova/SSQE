from modules.ui.page_objects.start_page_epam import StartEpamPage
import pytest

@pytest.mark.epamui
def test_check_the_title_is_correct():
    # Create object page
    start_page_epam = StartEpamPage()

    #Open page epam.com
    start_page_epam.go_to_epam()

    #Compare the title
    assert start_page_epam.check_epam_title("EPAM | Software Engineering & Product Development Services")

    #Close the browser
    start_page_epam.close()

@pytest.mark.epamui
def test_the_ability_to_switch_theme():
    # Create object page
    start_page_epam = StartEpamPage()

    #Open page epam.com
    start_page_epam.go_to_epam()

    initial_theme = start_page_epam.get_theme()
    print("Initial Theme:", initial_theme)

    # Step 2: Switch the theme
    start_page_epam.toogle_switch_elem()

    # Step 3: Check the switched theme
    switched_theme = start_page_epam.get_theme()
    print("Switched Theme:", switched_theme)

    # Verify the theme switch
    assert initial_theme != switched_theme, "Theme switch verification failed"

    # Close the browser
    start_page_epam.quit_driver()


@pytest.mark.epamui
def test_that_allow_to_change_lang_to_ua():
    # Create object page
    start_page_epam = StartEpamPage()

    #Open page epam.com
    start_page_epam.go_to_epam()

    #Find location and open
    start_page_epam.get_lang_location()

    start_page_epam.change_language()

    start_page_epam.check_epam_title("EPAM Ukraine - найбільша ІТ-компанія в Україні | Вакансії")
    
    start_page_epam.check_header_title("ВАКАНСІЇ")
    start_page_epam.check_header_title("НАВЧАННЯ")
    start_page_epam.check_header_title("БЛОГ")
    start_page_epam.check_header_title("ВАКАНСІЇ")
    start_page_epam.check_header_title("ПОДІЇ")
    start_page_epam.check_header_title("ПРО КОМПАНІЮ")
    
    start_page_epam.quit_driver()