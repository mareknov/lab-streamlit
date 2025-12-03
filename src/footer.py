import streamlit as st


def show_footer():
    """
    Display an informational footer about ski touring in Tatras with specific guidelines and safety recommendations.

    This function renders a comprehensive footer section for users planning alpine tours in the Tatras mountains, including general advice, seasonal information, and safety protocols. The content is designed to be displayed at the end of relevant pages or applications.

    The markdown output includes:
    - A divider line
    - An attention-grabbing header with an emoji icon
    - Multiple bullet points for key recommendations (formatted as list items)
    - Important guidelines about mandatory equipment certification requirements
    - Seasonal information specifying operational periods based on weather conditions
    - Critical safety advice regarding avalanche forecasts

    The footer is compiled from authoritative sources including adventure touring guides and trail databases, ensuring accurate representation of industry standards while being clearly presented to end-users.
    """
    # Footer
    st.markdown("---")
    st.markdown("<h3 style='text-align: center;'>📝 Important Notes</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center;'>

    All ski touring in the Tatras requires appropriate equipment and experience

    Alpine tours should be done with certified mountain guides

    Season: December 15 - April 15 (conditions permitting)

    Always check avalanche forecasts before heading out

    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<h4 style='text-align: center;'>📚 Data Sources</h4>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center;'>

    Trail data compiled from:
    
    [Slovakia.travel - Ski Mountaineering](https://slovakia.travel/en/ski-mountaineering)
    
    [Visit Liptov - Ski Touring Routes](https://www.visitliptov.sk/en/)
    
    [Rajec Travel - Ski Touring in Slovakia](https://www.rajectravel.sk/en/ski-touring-slovakia/ski-touring-in-slovakia-the-best-of-the-slovak-mountains/)
    
    [Adrop.cz - Best Skimo Locations in Slovakia](https://www.adrop.cz/en/blog/the-best-skimo-locations-in-slovakia)
    
    [Outdooractive - Ski Touring Routes Slovakia](https://www.outdooractive.com/en/ski-tours/slovakia/)

    </div>
    """, unsafe_allow_html=True)
