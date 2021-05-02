from find_data import find_data, get_text_strip

def Data_extract(soup):
    info = []
    print(soup)
    Profile_name = find_data(soup,'div', 'top-card-layout__entity-info-container')
    info.append(get_text_strip(Profile_name))
    
    Summary = find_data(soup,'section', 'summary pp-section')
    info.append(get_text_strip(Summary))

    Education = find_data(soup,'section','education pp-section')
    info.append(get_text_strip(Education))

    Courses =find_data(soup,'section','courses pp-section')
    info.append(get_text_strip(Courses))

    Projects = find_data(soup,'section','projects pp-section')
    info.append(get_text_strip(Projects))

    Languages = find_data(soup,'section','languages pp-section')
    info.append(get_text_strip(Languages))

    Groups = find_data(soup,'section','groups pp-section')
    info.append(get_text_strip(Groups))

    Others = find_data(soup,'section','bottom-cta-banner')
    info.append(get_text_strip(Others))

    Searched = find_data(soup,'section','browsemap right-rail-section')
    info.append(get_text_strip(Searched))

    Other_users_same_name = find_data(soup,'section','samename right-rail-section')
    info.append(get_text_strip(Other_users_same_name))

    Course_recommendation = find_data(soup,'section','course-recommendations right-rail-section')
    info.append(get_text_strip(Course_recommendation))

    Badges_earned = find_data(soup,'section','badge right-rail-section')
    info.append(get_text_strip(Badges_earned))
    
    return info