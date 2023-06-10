import streamlit as st
import requests

def main():
    st.title("🚀 Workmate APP ")
    st.subheader("💡 Making life easy for disables ")

    file_url = "https://github.com/devil99990/streamlit-example/blob/9d7c2a449b540679f17358df834d6f25da2ff0c0/file.zip"  # Replace with the actual file URL on GitHub

    # Download button
    download_button = st.button("📥 Download App ")

    if download_button:
        download_file(file_url)

    st.image("https://th.bing.com/th/id/OIG.AkWDJT53uVtTInAx3SNh?pid=ImgGn", use_column_width=True)

    st.sidebar.header("About")
    st.sidebar.markdown("The web app, **Workmate**, developed by GH Raisoni College of Engineering Nagpur students, aims to make life easier for blind and disabled individuals by leveraging advanced AI and ML technologies. It provides various features, including eye moment and voice command-based computer usage : ")

    with st.sidebar.expander("Features"):
        st.sidebar.markdown("- Voice command-based computer usage")
        st.sidebar.markdown("- Eye movement-based mouse control")
        st.sidebar.markdown("- High-security face recognition")

    with st.sidebar.subheader("Health Equipment for Disabled Individuals"):
        st.sidebar.markdown("For disabled individuals, having access to the right health equipment is crucial. Here are some recommended products available on Amazon: ")

        st.sidebar.subheader("Wheelchairs")
        st.sidebar.markdown("- [Wheelchair 1](https://www.amazon.com/wheelchair-1)")
        st.sidebar.markdown("- [Wheelchair 2](https://www.amazon.com/wheelchair-2)")
        st.sidebar.markdown("- [Wheelchair 3](https://www.amazon.com/wheelchair-3)")

        st.sidebar.subheader("Mobility Aids")
        st.sidebar.markdown("- [Mobility Aid 1](https://www.amazon.com/mobility-aid-1)")
        st.sidebar.markdown("- [Mobility Aid 2](https://www.amazon.com/mobility-aid-2)")
        st.sidebar.markdown("- [Mobility Aid 3](https://www.amazon.com/mobility-aid-3)")

    with st.sidebar.subheader("Assistive Devices for Blind Individuals"):
        st.sidebar.markdown("Blind individuals can benefit from various assistive devices. Here are some recommended products available on Amazon: ")

        st.sidebar.subheader("Braille Displays")
        st.sidebar.markdown("- [Braille Display 1](https://www.amazon.com/braille-display-1)")
        st.sidebar.markdown("- [Braille Display 2](https://www.amazon.com/braille-display-2)")
        st.sidebar.markdown("- [Braille Display 3](https://www.amazon.com/braille-display-3)")

        st.sidebar.subheader("Talking Watches")
        st.sidebar.markdown("- [Talking Watch 1](https://www.amazon.com/talking-watch-1)")
        st.sidebar.markdown("- [Talking Watch 2](https://www.amazon.com/talking-watch-2)")
        st.sidebar.markdown("- [Talking Watch 3](https://www.amazon.com/talking-watch-3)")

def download_file(file_url):
    response = requests.get(file_url, stream=True)

    if response.status_code == 200:
        with open("file.zip", "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        st.success("✅ To  downloaded APP successfully! >>CLICK ON BELOW DOWNLOAD BUTTON ")
        st.write ("after Downloading of file export the file and run App.exe ")
        # Prompt user to select download location
        file_path = "./file.zip"
        with open(file_path, "rb") as f:
            st.download_button(
                label="📥 Click here to download the Application ",

                data=f,
                file_name="file.zip"
            

            )
    else:
        st.error("❌ Failed to fetch file from URL")

if __name__ == "__main__":
    main()
