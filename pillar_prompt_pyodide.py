def get_filled_prompt_template(
        topic,
        client_name,
        client_url,
        client_logo_url,
        client_contact_info,
        tone,
        style,
        expertise_level,
        client_positioning,
        target_audience,
        core_topics
):
    core_topics_fmt = "\n".join([f'    - {topic}' for topic in core_topics])
    template = f"""
    Create a comprehensive {topic} guide of approximately 5,000 words for {client_name} (website: {client_url}) that aligns with their brand voice characterized by:

    ## Brand Voice Elements:
    - Tone: {tone}
    - Language Style: {style}
    - Expertise Level: {expertise_level}
    - Client Positioning: {client_positioning}
    - Target Audience: {target_audience}

    The guide should use the hook pacing method to maintain reader engagement throughout. Each section should open with a compelling hook, provide detailed context, and lead naturally to the next section. The guide should:

    1. Content Structure:
    - Begin with an immediate emotional hook addressing the reader's urgent need
    - Use mini-hooks at the start of each major section
    - Include story-driven transitions between sections
    - Build anticipation for upcoming information
    - Create strategic information reveals
    - End sections with subtle cliffhangers that drive continued reading

    2. Content Style:
    - Blend narrative elements with practical information
    - Expand bullet points into contextual paragraphs
    - Use real scenarios to introduce complex topics
    - Include expert insights and perspectives
    - Maintain a supportive, authoritative tone
    - Balance emotional understanding with practical guidance

    3. Core Topics (each with narrative context):
{core_topics_fmt}

    4. Enhanced Features:
    - Opening scenario that captures reader attention
    - Case studies that illustrate key points (with privacy notices)
    - Process explanations with context
    - Resource sections with implementation guidance
    - FAQ section addressing emotional and practical concerns

    5. Technical Elements:
    - SEO optimization while maintaining readability
    - Schema markup for rich snippets with client details:
    * Organization name: {client_name}
    * Website: {client_url}
    * Logo URL: {client_logo_url}
    * Contact information: {client_contact_info}
    - Clear heading hierarchy
    - Internal linking structure to relevant client content
    - Client-specific meta descriptions and titles

    6. Branding Elements:
    - Incorporate client expertise markers
    - Reference client-specific services where relevant
    - Include client case examples (anonymized)
    - Use client's preferred terminology
    - Maintain consistent voice across all sections

    7. Call-to-Action Integration:
    - Client-specific contact methods
    - Service-related offers
    - Consultation booking information
    - Resource access points
    - Newsletter signup if applicable

    Each section should:
    - Open with a compelling hook
    - Provide thorough context
    - Include practical guidance
    - Offer actionable steps
    - Lead naturally to the next topic
    - Maintain emotional engagement while delivering crucial information
    - Reinforce client expertise and authority

    The guide should feel like a conversation with {client_name}'s expert team, conveying their unique value proposition while delivering comprehensive, practical information.

    Additional requirements:
    - Include all schema markup elements
    - Add comprehensive FAQ section
    - Include meta description
    - Include social sharing elements
    - Include all technical SEO elements
    - Include client boilerplate for bio section
    - Add client-specific disclaimers where needed

    Please proceed with creating the full guide, maintaining consistent engagement throughout while delivering comprehensive, practical information that positions {client_name} as the authoritative source in their field.
    """

    return template


form_input = _input.all().to_py()[0]
data = form_input["json"]["body"]

filled_prompt = get_filled_prompt_template(**data)

return [{"prompt": filled_prompt}]
