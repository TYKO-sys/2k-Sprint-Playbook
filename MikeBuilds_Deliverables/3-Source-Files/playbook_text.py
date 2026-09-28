# playbook_text.py - full content for The $2K Sprint Playbook
# Voice: conversational, short sentences, empathetic, no banned phrases.
# Block types: ("p", text) | ("h2", text) | ("bullets", [..]) |
#   ("table", dict(headers, rows, ratios)) | ("callouts", [(big, label), ..]) |
#   ("chart", None) | ("caption", text)

CHAPTERS = [
# ---------------------------------------------------------------- CHAPTER 1
{
"title": "The Verdict",
"blocks": [
("p", "Here is the situation in plain numbers. You need $2,000. You have eight weeks, a Windows laptop, six focused hours a day, and zero dollars to spend. No audience. No portfolio. No warm network. What you do have is a vibe coder's hands, a US payment rail, and a willingness to get on calls. That is enough. This chapter says where the money will come from and what has to be true for it to arrive."),
("p", "The plan runs on three lanes at once. Lane A is the cash engine: you build automations for small businesses and charge $400 to $800 per build, then stack $50 to $100 monthly retainers on top. Lane B is the fast-cash ladder: Fiverr and Upwork gigs built on the same free tools, priced to land your first orders inside two weeks. Lane C is the slow burn: every client build becomes a template you sell on Gumroad. Three lanes, one stack. Nothing new to buy. Nothing new to learn that you cannot learn by building."),
("p", "The market data says this is real, not theoretical. Agencies charge $1,500 to $10,000 to build what n8n does for free. Workflow automation gigs on Upwork run $500 to $2,000. AI receptionist services bill $297 a month as a standard rate. You will charge less than all of them, because you are new, and you will raise prices after your second close. Underpricing is your foot in the door. It is not your permanent condition."),
("callouts", [("$0", "total cost of the entire tool stack"), ("$500-2,000", "market rate per workflow build"), ("$297/mo", "standard rate for an AI receptionist")]),
("p", "Honest odds, because you deserve them: at full sprint discipline, the expected band lands between $1,600 and $2,700 by week eight. That is roughly a coin flip to clear $2,000, tilted in your favor if you hold volume daily and close your first deal by week four. Three things move the number: how many conversations you start, how fast the first close happens, and whether you ask for the retainer every single time. Volume is the one you control most. Volume is therefore the one that matters most."),
("p", "Read the next chapter with your links open. Everything recommended here traces back to something you already sourced. You did the digging. This book just points at what pays."),
]},
# ---------------------------------------------------------------- CHAPTER 2
{
"title": "Your Free Arsenal",
"blocks": [
("p", "You handed me four resources. I read all four. The fmhy AI page is a wall of free chatbots, image generators, voice tools, and video engines. Your curated catalog is the bigger find: 199 verified GitHub repos pulled from 361 posts, with 97 candidates in agents and automation alone. The Linux/macOS page maps the self-hosting ecosystem. The misc page hides the distribution channels. Here is what actually matters for making money."),
("table", {
  "headers": ["Tool", "What it is", "What it earns"],
  "ratios": [0.18, 0.40, 0.42],
  "rows": [
    ["n8n", "Self-hosted workflow automation with built-in AI agent nodes", "The builds you sell in Plan A, $400-800 each"],
    ["OpenSEO", "Open-source alternative to Semrush and Ahrefs", "SEO audit reports, $250-500 one-off plus monitoring"],
    ["Scrapling", "Adaptive web scraper that survives site layout changes", "Self-refilling lead lists you sell or use"],
    ["changedetection.io", "Website change monitoring with alerts", "Competitor and price watchtowers, $99-199/mo"],
    ["Postiz", "Agentic social media scheduling tool", "Content systems you run for up to five clients"],
    ["Pipecat", "Open-source framework for voice agents", "AI receptionist lines at $197-297/mo"],
  ]}),
("caption", "Table 1: The six core tools, verified live on GitHub. All free, all self-hostable."),
("p", "The support cast matters too. Cal.com gives you a free booking link so clients schedule calls without email ping-pong. Gumroad hosts your digital products with zero setup fees. yt-dlp pulls source video for clip work. auto-editor cuts silence from long recordings in one command. And the free tiers from your fmhy AI page cover your writing, coding, and research needs without touching a credit card. Your catalog also carries Pipecat, Postiz, and a voice-agent stack, so most of this spine came from your own sourcing."),
("p", "One rule, and I need you to take it seriously. Some links on fmhy point at cracked or ToS-violating access to paid tools. Skip those. Build only on legit free tiers and open source. This is not a moral lecture. It is arithmetic. A business running on gray tools dies the day an account gets banned, and you do not get a second account when your income depends on it. Everything in this book runs clean. Keep your stack that way and you never have to explain an outage you caused."),
("p", "A 24GB Mac is coming your way. Good news: everything above runs on both machines. n8n ships as a Docker container, so your workflows export from Windows and import on macOS in one afternoon. The Mac's extra RAM unlocks local models through Ollama or LM Studio, both listed on your fmhy AI page - free AI with no rate limits. That is a later upgrade, not a day-one need. Do not wait for the Mac to start. The clock is already running."),
]},
# ---------------------------------------------------------------- CHAPTER 3
{
"title": "Plan A: The Automation Mechanic",
"blocks": [
("p", "Small businesses drown in repetitive work. Missed leads. Unanswered reviews. Invoices that never get chased. A phone that rings into silence at 6pm. You are going to sell them back their time, one workflow at a time. n8n is your factory. The client never needs to know their $600 system runs on free software. They are paying for the outcome and the setup, and that is a fair trade."),
("h2", "The offer menu"),
("table", {
  "headers": ["Offer", "What the client gets", "Price", "Build time"],
  "ratios": [0.24, 0.40, 0.18, 0.18],
  "rows": [
    ["Lead capture system", "Form or DM lands, AI qualifies it, CRM sheet updates, you get a text alert", "$400-800", "1 day"],
    ["Review automation", "New review detected, AI drafts a reply, owner approves by text, it posts", "$300-600", "1 day"],
    ["Invoice chaser", "Due dates checked nightly, polite escalation sequence, payment link attached", "$300-500", "Half day"],
    ["AI receptionist", "24/7 answering line that books appointments and answers common questions", "$197-297/mo", "2-3 days"],
    ["SEO audit report", "Rank tracking, site audit, keyword gaps, branded PDF deliverable", "$250-500", "Half day"],
  ]}),
("caption", "Table 2: Plan A offer menu. Prices sit under agency rates on purpose."),
("h2", "Pick one niche"),
("p", "Pick one niche for the first 30 days. Home services are the classic play: roofers, HVAC, plumbers, med spas, dentists. They have cash, they have pain, and their competitors are slow to adopt anything. One niche means one offer menu, one demo reel, and one set of objections to learn. Spreading across five niches in week one means learning five businesses at once. That is a treadmill, not a strategy. Depth first. Breadth later, when the retainer stack pays for it."),
("h2", "Demo first, ask second"),
("p", "Build two spec demos before you send a single email. A lead-capture flow for a fake roofing company. A review automation for a fake med spa. Record a 90-second Loom walking through each one, screen only, no face needed. Now your cold email is not a promise. It is a link. Links close deals that promises cannot, because a working demo answers the only question a skeptical owner has: can this person actually do it?"),
("h2", "The math that makes it boring"),
("p", "The volume math is boring and reliable, which is exactly what you want. Twenty-five personalized emails a day, five days a week, is 125 touches a week. At a 3-5% reply rate that is four to six conversations weekly. One in four or five conversations becomes a call. One in two or three calls closes. First close lands in week three or four if outreach starts in week two. Every number here is a floor, not a ceiling. Skip a day of outreach and the pipeline skips you right back."),
("h2", "Price like a newcomer, raise like a survivor"),
("p", "Market rates run $1,500 to $10,000 per build. You will charge $400-800 to start. That is not insecurity. That is strategy. Your first two clients are buying a discount and forgiving your rough edges. Client three pays full rate because clients one and two left testimonials. After two closes, raise prices 30%. After four, stop quoting under $1,000. Your calendar fills, your prices climb, and the same hour of work pays triple. That is the whole game."),
("p", "Then ask for the retainer every single time. Say it like this: I will keep this running, watch for breaks, and update it as your business changes, $75 a month. Half will say yes. Retainers are the difference between a $2,000 month and a $2,000 business. The ones who decline still keep your number."),
]},
# ---------------------------------------------------------------- CHAPTER 4
{
"title": "Plan B: The Gig Ladder",
"blocks": [
("p", "Fiverr and Upwork are unfair to newcomers and fair to the persistent. The first three weeks feel like shouting into a void. Then the reviews land, the algorithm notices, and orders arrive while you sleep. Your gigs use the same stack as Plan A, which means every completed order doubles as portfolio proof for your cold outreach. Two lanes feeding each other beats two lanes racing separately."),
("table", {
  "headers": ["Gig", "Price anchor", "Notes"],
  "ratios": [0.28, 0.20, 0.52],
  "rows": [
    ["n8n workflow build", "$150-600", "Highest demand. Mirror the exact titles buyers search for."],
    ["AI chatbot setup", "$50-200", "Fast delivery. Cheap gigs feed the review engine."],
    ["Data scraping service", "$100-400", "Scrapling under the hood. Sell the list, never the tool."],
    ["Website monitoring setup", "$100-250", "changedetection.io. Pitch it as: know before your customers do."],
    ["SEO audit report", "$150-400", "OpenSEO output, branded PDF, 48-hour turnaround."],
  ]}),
("caption", "Table 3: Plan B gig lineup. Five listings, one shared tool stack."),
("p", "Ranking tactics that actually move the needle: run three gigs at most, because focus ranks better than spread. Write keyword-loaded titles - I will build n8n automation with AI agents beats automation expert every time. Record a 30-second video intro for each gig; conversion roughly triples and your phone camera is enough. Reply to every buyer message inside one hour while you are awake. Price the first five orders about 40% under target to buy reviews, then raise. Fiverr's algorithm forgives slow starts. It never forgives silence."),
("p", "Upwork plays differently. Bid on $500-2,000 workflow projects with a proposal that leads with a Loom demo of a similar build. Buyers there pay for proof, not promises. Ten proposals a week, each opening with a custom paragraph that references their specific job post, outperforms a hundred generic blasts. Your vibe-coder skills matter most on this platform, because clients pay real money the moment you can show working code instead of describing it."),
]},
# ---------------------------------------------------------------- CHAPTER 5
{
"title": "Plan C: The Product Flywheel",
"blocks": [
("p", "Products are where money stops trading hours for dollars. One template sells at 2am while you sleep. But there is a rule with no exceptions: no product before two client builds exist. Not because templates are hard to make - because selling templates with zero proof is hard. Built for a real roofing company outsells theoretical lead funnel every single time. Your first two clients are your product research department, whether they know it or not."),
("p", "Here is the product line that falls out of Plan A naturally. The n8n lead-capture workflow becomes a $29-49 template. The AI receptionist setup guide sells at $19-39. The prompt pack that runs your review automation goes for $9-19. The offer menu itself, rebranded as an Automation Menu for Agencies, sells at $49. Every item is a byproduct of work you already did for pay. The inventory costs you an export command."),
("p", "Gumroad hosts all of it with zero setup fees. They take a cut per sale and you risk nothing. Distribution is the real game, and your own links point the way: the fmhy misc page lists a directory of 280+ websites to submit your startup - treat that as your launch checklist. Product Hunt gives you a one-day spike if you time it for a Tuesday or Wednesday. Short demo clips on TikTok and YouTube Shorts show the workflow actually running, and each clip ends on the Gumroad link. Clips are the new storefront window."),
("p", "Set expectations now, so week six does not discourage you: $200-500 inside the eight-week window is the honest band. Products compound slowly, then suddenly. Month three is where a small catalog starts paying rent. Treat Plan C as the asset you build while Plans A and B pay the bills. That is not a consolation prize. That is the exit ramp from freelancing, built with the same hours you were already working."),
]},
# ---------------------------------------------------------------- CHAPTER 6
{
"title": "The $2,000 Math",
"blocks": [
("p", "Every week has a focus and a target. If a week lands short, the fix is almost always more conversations, not more building. Builders hide in building. Sellers count money. Here is the full board, three scenarios deep."),
("table", {
  "headers": ["Week", "Focus", "Conservative", "Expected", "Aggressive"],
  "ratios": [0.10, 0.50, 0.13, 0.13, 0.14],
  "rows": [
    ["1", "Setup, demo builds, accounts, email warmup begins", "$0", "$50", "$150"],
    ["2", "Outreach begins, all five gigs live", "$0", "$250", "$500"],
    ["3", "First conversations, first gig orders land", "$150", "$400", "$900"],
    ["4", "First Plan A close and delivery", "$350", "$700", "$1,200"],
    ["5", "Second close, retainer asks begin", "$600", "$1,000", "$1,700"],
    ["6", "Retainers stack, gig flow steadies", "$900", "$1,400", "$2,200"],
    ["7", "Product launch, third close", "$1,200", "$1,750", "$2,700"],
    ["8", "Collect, upsell, stabilize the floor", "$1,600", "$2,250", "$3,300"],
  ]}),
("caption", "Table 4: Cumulative revenue by week, three scenarios. Figures are cash collected, not promises."),
("chart", None),
("caption", "Figure 1: Cumulative revenue curves for the three scenarios. The gap between conservative and expected is mostly outreach volume."),
("h2", "Decision rules, because feelings lie"),
("bullets", [
  "Zero replies after 250 emails: the niche or the channel is wrong. Change exactly one of them, never both at once.",
  "Two closes by week five: raise prices 30% today. Demand is telling you something. Listen to it.",
  "No gig order within 21 days: rewrite the title, rerecord the video, swap the thumbnail. Same stack, new packaging.",
  "Four retained clients at $75: that is $300 a month arriving whether you close anyone new or not. That is your floor. Stack floors.",
  "Two late nights in a row: take the next morning off. Burnout math is brutal; one lost week costs more than one rest day.",
]),
("p", "The scenarios differ less in skill than in stubbornness. The conservative line assumes you send most of your daily emails and close one in six conversations. The aggressive line assumes you never miss a day, close one in three, and land two retainers early. Same tools. Same offers. The dial is discipline, and discipline is free."),
]},
# ---------------------------------------------------------------- CHAPTER 7
{
"title": "The Apprenticeship",
"blocks": [
("p", "Five stages, beginner to owner. Each stage carries tasks, a drill, uncommon resources, and one shortcut that saves you a week. The drills are simulations - safe fake versions of the real thing, run until the real thing stops being scary. That is how pilots train. It works for operators too."),
("h2", "Stage 1 - Novice: install the factory (days 1-3)"),
("p", "You are not learning automation in the abstract. You are installing a factory. By the end of day three, n8n runs on your machine, your accounts exist, and your email warmup has begun. Nothing gets sold yet. Foundations first."),
("bullets", [
  "Install Docker Desktop, then run n8n as a container. The npm route works too if Docker fights you.",
  "Create a business Gmail. This address becomes your outreach engine, so it never touches personal mail.",
  "Set up Cal.com with a booking link, plus Fiverr, Upwork, and Gumroad accounts. One sitting, all five.",
  "Start email warmup: 10-20 normal emails a day to friends, newsletters, anything real. Volume ramps later.",
  "Bookmark the free AI tiers from your fmhy AI page - DeepSeek, Gemini, ChatGPT, Claude. These are your analysts.",
]),
("p", "Drill: the 30-minute flow. Build webhook to Google Sheet to email notification from a blank canvas, timer on. You will fail the first time. Build it again. The second build is the skill. Shortcut: clone, do not create. The n8n community library holds hundreds of free workflows. Import one, dissect it node by node, rebuild it blank. Learning by autopsy beats blank-page heroics ten times out of ten."),
("h2", "Stage 2 - Operator: build ammunition (days 4-10)"),
("p", "Operators ship. Ten days from now you hold three demo builds, one real SEO audit, and a lead list with fifty real businesses on it. None of it is client work yet. All of it is ammunition, and ammunition is what closes deals later."),
("bullets", [
  "Build the lead-capture demo for a fake roofing company. Webhook in, AI qualification, sheet, text alert.",
  "Build the review automation demo for a fake med spa. Detection, AI draft, approval text, post.",
  "Run one real OpenSEO audit against a local business site you picked at random. Keep the branded PDF.",
  "Pull 50 local business leads with Scrapling. Name, site, email, one observed fact each.",
  "Record 90-second Looms for both demos. Screen only. Talk like you talk.",
]),
("p", "Drill: rebuild the lead-capture flow from memory, no template, under 45 minutes. Stuck? Note where, look it up, finish, then restart from scratch. Reps beat references. Shortcut: record while you build. Every build session produces demo footage at zero extra cost. The footage is the sales asset you will reuse for months."),
("h2", "Stage 3 - Sales apprentice: talk to strangers (weeks 2-3)"),
("p", "Now you learn the skill that pays: talking to strangers about their problems. Your demos do the proving. You do the talking. Volume starts low and ramps with your warmup, so the machine grows while you do."),
("bullets", [
  "Write the offer menu and the Loom script. Read the script twice, then throw it away and just show the demo.",
  "Build the outreach sheet: 50 leads, one personalized first line each. Observation, not flattery.",
  "Send 25 emails a day, every workday. Log replies, calls, closes. The sheet is your scoreboard.",
  "Run mock discovery calls until 'how much?' stops spiking your pulse.",
  "Write your objection list: too expensive, tried it before, too busy, my nephew does computers. Answer each in one sentence.",
]),
("p", "Drill: role-play the discovery call with an AI. Prompt it: you are a skeptical roofer with six employees, annoyed by technology, worried about cost. Ask me hard questions. Run it out loud, ten times. Shortcut: answer the money question with a range and a reason. $400 to $800 depending on complexity, most clients land in the middle. Ranges feel honest. Single numbers feel like an invitation to haggle."),
("h2", "Stage 4 - Closer: deliver like a pro (weeks 3-6)"),
("p", "First client. The fear is real and useless in equal measure. Delivery is a checklist, not a talent show. Run the same five steps every time and clients experience you as organized, calm, and worth referring."),
("bullets", [
  "Step 1: kickoff form. Eight questions. Their tools, their goals, their login for the pieces you connect.",
  "Step 2: build on staging, never live. Show nothing until it runs clean twice.",
  "Step 3: the 15-minute walkthrough call. Screen share. Let them press the button.",
  "Step 4: tweak day. One round of changes, written down, done within 48 hours.",
  "Step 5: handoff doc plus the retainer pitch, delivered together, same email.",
]),
("p", "Drill: dry-run delivery on your fake roofing demo as if a real client paid. Fill the kickoff form yourself, deliver on schedule, write the handoff doc with a logo on top. The rehearsal deletes half the first-client panic. Shortcut: the handoff doc doubles as a product. Client-ready, branded, screenshot in the middle - that is Gumroad inventory by week six."),
("h2", "Stage 5 - Owner: become the exception (weeks 6-8)"),
("p", "Owners stop doing everything themselves. Your systems now run outreach, delivery, and follow-up with you as the exception, not the rule. Two weeks of systemizing turns a hustle into something you could hand off."),
("bullets", [
  "Productize your best build as a Gumroad template. Launch through the 280+ submission directory from your misc page.",
  "Load two weeks of content into Postiz. Demo clips, build timelapses, client wins. Queue it, forget it.",
  "Write your SOPs: outreach, delivery, onboarding. One page each. If it repeats twice, it gets a page.",
  "Plan the Mac migration: export Docker volumes, push configs to a private repo. Afternoon job, not a project.",
  "Raise prices. Yes, again. The calendar says so.",
]),
("p", "Drill: the four-hour week test. Pick a normal Tuesday and log every minute. Anything that repeated twice becomes a checklist or an n8n flow. This drill is the difference between a hustle and a company. Shortcut: never migrate mid-sprint. Land week seven and eight revenue on Windows. Move to the Mac on a calm weekend with zero live deadlines and a finished export."),
("p", "Past week eight, the moves change. Hire a part-time VA for outreach ops at a fair hourly rate. Verticalize into one industry until they know your name. Push builds past $1,500. Package retainers at $300-500 a month. The ceiling moves when you do. Mastery here is not a certificate. It is a stack of systems that earn while you are busy elsewhere."),
]},
# ---------------------------------------------------------------- CHAPTER 8
{
"title": "The Outreach Playbook",
"blocks": [
("p", "Cold outreach is a fuel. Burn it wrong and you torch your sender reputation for months. Burn it right and it runs the whole engine. The safe middle wins: fewer messages, sharper openers, warmed accounts. You chose this lane yourself, so here is exactly how it works."),
("h2", "Warmup before volume"),
("table", {
  "headers": ["Days", "Daily sends", "What goes out"],
  "ratios": [0.18, 0.22, 0.60],
  "rows": [
    ["1-3", "5-10", "Personal emails only. Replies to real threads. No pitching."],
    ["4-7", "15", "Mostly personal, a few newsletters you actually read."],
    ["8-14", "25-30", "First cold sends mixed in, fully personalized, no links."],
    ["15+", "30 cap", "Hold the cap. Growth past this needs a second warmed inbox."],
  ]}),
("caption", "Table 5: The 14-day warmup ramp. Skipping it is how good offers die in spam folders."),
("h2", "Legal in three lines"),
("p", "CAN-SPAM is simpler than people fear. Identify yourself honestly. Include a working unsubscribe line in every cold email. List a physical address in the footer. Do those three things and you are compliant. Skip them and each email risks a fine up to $46,517, which converts a $75 retainer into a very bad trade. Compliance here costs ninety seconds per send."),
("h2", "The opener formula"),
("p", "One observed fact. One implication. One offer. Saw your crew repave Elm Street last week, nice work. Noticed nobody answers your Google reviews though, three sit unanswered since August. I built a system that auto-drafts replies for your approval, want the 90-second demo? That is the whole formula. Observation beats flattery. Specific beats generic. A link to a working demo beats every adjective you were going to use."),
("h2", "Follow-up without begging"),
("p", "Three touches, then stop. Day three: one line, new angle. Day seven: the demo link again, no apology for following up. Day twelve: the door-closer, closing my list this week, want in or should I check back next quarter? Then silence. Silence protects the account and, frankly, your dignity. Most replies come from touch two. Most closers come from touch three. But the list ends at three."),
("p", "For local businesses, Instagram and Facebook DMs often outperform email. Ten a day, no more. Comment on their most recent post first, wait a day, then send: loved the driveway job. Quick question, who handles your online reviews? Softer, slower, better reply rates than cold email, and the account risk sits with you alone."),
("p", "Reality check for your expectations: 2026 inbox rates average 71%. Nearly three in ten cold emails vanish before any human sees them. That is why volume without personalization is dead weight. One real sentence about their actual business lifts you out of the spam folder more reliably than any technical trick. Write like a neighbor, not a marketing department."),
]},
# ---------------------------------------------------------------- CHAPTER 9
{
"title": "The Automation Dial",
"blocks": [
("p", "Here is the honest map of what runs itself and what needs your hands. The dial turns over eight weeks: more machines, less you. Nothing on this table requires paid software, and every automation listed is something you already built as a demo in Stage 2. You are not adding work. You are converting work you already did into work that repeats without you."),
("table", {
  "headers": ["Task", "Weeks 1-2", "Week 8 and beyond"],
  "ratios": [0.34, 0.30, 0.36],
  "rows": [
    ["Lead sourcing", "Manual pulls, 50 at a time", "Nightly Scrapling run, sheet refills itself"],
    ["Personalized first lines", "You write every one", "AI drafts from the lead sheet, you approve"],
    ["Follow-up sequences", "Sent by hand, tracked in sheet", "n8n fires day 3, 7, 12 automatically"],
    ["Monitoring reports", "Not running yet", "changedetection.io weekly PDF, branded"],
    ["SEO audits", "Run manually per client", "Scheduled, generated, delivered on autopilot"],
    ["Social posting", "Nothing", "Postiz queue, two weeks deep"],
    ["Product delivery", "Not applicable", "Gumroad sends it instantly, forever"],
    ["Discovery calls", "You, and that is fine", "You. This one stays human on purpose."],
    ["Closing", "You", "You. The trust layer never fully automates."],
    ["Build quality checks", "You, twice per build", "You, once per build, with a checklist"],
  ]}),
("caption", "Table 6: What automates and what stays human. The human column is the moat."),
("p", "The layer that never fully automates is the trust layer. Calls, closes, quality checks. That is not a flaw in the plan. That is the moat. Anyone can rent the same free tools. Almost nobody will do the human 20% that makes clients stay, refer, and renew. Automate the boring 80% so you have the energy to be excellent at the 20% that machines cannot fake."),
("p", "On the Mac migration: keep everything in Docker from day one and keep nothing important on the desktop. Export volumes weekly, push configs to a private GitHub repo, and the eventual move becomes an afternoon instead of a funeral. When the 24GB machine lands, Ollama or LM Studio turns it into a local AI box with no rate limits - the moment your automation costs drop to literally zero per task."),
]},
# ---------------------------------------------------------------- CHAPTER 10
{
"title": "Risks and Gray Zones",
"blocks": [
("p", "Ranked by how often they kill plans exactly like this one. Read the list twice, then check it again at week four. Every failure mode here has an early warning signal, and every signal has a response that costs less than the failure."),
("bullets", [
  "Silence. 250 emails, zero replies. Signal: your offer, niche, or list is wrong. Response: change one variable, keep the volume.",
  "Anchoring too low for too long. Two closes came and went, prices stayed flat. Response: raise 30% the day the second close lands.",
  "Scope creep. The $600 build became a $600 platform. Response: the tweak day exists precisely so extra work has a price tag.",
  "Deliverability death. Sends land, nothing arrives. Response: pause seven days, warm again slowly, check the unsubscribe line.",
  "Gig account bans. Fiverr punishes off-platform payment talk instantly. Response: keep every conversation inside the platform.",
  "Burnout. Two skipped days becomes four. Response: the morning-off rule. Rest is a scheduled task, not a failure state.",
]),
("p", "Now the gray zone, in plain words. Your fmhy links include tools that unlock paid software without paying. Some of them work. All of them carry ban risk, and income built on a bannable account is income on a timer. Client work has a second problem: gray tools inside a client's stack become your liability the day they break at 9am on a Monday. Keep client stacks clean, keep your own clean, and you never explain an outage you caused. This is the cheapest insurance in the book, and it costs nothing but restraint."),
("p", "Time-wasters to refuse for eight straight weeks: crypto flips need capital you do not have. Dropshipping needs ad spend. Affiliate SEO needs six months you do not have. AI wrapper startups need funding and luck in equal measure. Every one of them will whisper at you in week three, when outreach feels slow and shiny things look bright. Say no to all of them. Focus is the cheapest advantage you own, and it is the only one nobody can copy."),
]},
# ---------------------------------------------------------------- CHAPTER 11
{
"title": "This Week's Checklist",
"blocks": [
("p", "Seven days, one page, no excuses. Each day is sized for your six hours. Do the day's list, then stop. The plan works because it is ordinary. Ordinary, repeated daily, is what compounding looks like from the inside."),
("bullets", [
  "Day 1: Docker and n8n running. Business Gmail created. First warmup emails sent.",
  "Day 2: Cal.com, Gumroad, Fiverr, Upwork accounts live. Booking link tested end to end.",
  "Day 3: Lead-capture demo built. First 90-second Loom recorded and watched back once.",
  "Day 4: Review automation demo done. One real OpenSEO audit run on a local site.",
  "Day 5: Scrapling pulls 50 leads. Outreach sheet built, first line written for every lead.",
  "Day 6: Three Fiverr gigs live with video intros. Upwork profile and portfolio polished.",
  "Day 7: First 25 emails out before noon. Then close the laptop. Rest is on the list too.",
]),
("p", "The master rule that runs this whole book: ship ugly, ship early, fix it in front of the client. Perfect systems do not get paid. Working ones do, and they get paid first. Every tool in this arsenal came from links you sourced yourself, which means every dollar this plan earns traces back to work you already did before we ever met. See you at the first close."),
]},
]
